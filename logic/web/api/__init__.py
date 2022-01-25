from enum import unique
from posix import EX_TEMPFAIL
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config.from_object("api.config.Config")
db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(64), nullable=False, unique=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

    def __init__(self, email, name=""):
        self.email = email
        self.name = name

class User_api(Resource):

    def get(self):

        args_parser = reqparse.RequestParser()
        args_parser.add_argument('email', type = str)

        args = args_parser.parse_args()
        email = args['email']

        try:
            user_info = db.session.query(User).filter_by(email=email).first()
            return {'name': user_info.name, 'email': user_info.email}

        except:
            return {'ERROR': 'Email not found'}

    
    def post(self):

        args_parser = reqparse.RequestParser()
        args_parser.add_argument('email', type = str)
        args_parser.add_argument('name', type = str)

        args = args_parser.parse_args()
        email = args['email']
        name = args['name']

        try:
            db.session.add( User(email=email, name=name) )
            db.session.commit()
            return {'name': name, 'email': email}

        except:
            return {'ERROR': 'Email not found'}

api.add_resource(User_api, '/user')