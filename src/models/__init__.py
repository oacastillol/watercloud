from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()
from .SampleModel import SampleModel, SampleSchema
#from .UserModel import UserModel, UserSchema
