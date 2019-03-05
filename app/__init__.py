# import os
#
# import africastalking
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy




bootstrap = Bootstrap()
db = SQLAlchemy()



def create_app(config_name):


   app = Flask(__name__)
   # username = "sandbox"
   # api_key =
   # "a1751b190070fe558e4c9e715ac66e140fb632ed8420d6aeca789460f0699ff5"
   # africastalking.initialize(username, api_key)
   #
   # sms = africastalking.SMS

   app.config.from_object(config_options[config_name])

   bootstrap.init_app(app)

   db.init_app(app)

   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)

   from .auth import auth as auth_blueprint
   app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')


   return app
