from flask import request, json, Response, Blueprint, g, escape
#from ..models.UserModel import UserModel, UserSchema
from re import match
user_api = Blueprint('users', __name__)
user_schema = UserSchema()

"""
Se encarga de responder y manejar la información
de acceso de los usuarios
"""
