# third-party imports
import os
from  flask_jwt_extended import JWTManager
from datetime import timedelta
from flask import Flask
from .dbconect import init_db

# local imports
from config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config['JWT_SECRET_KEY']= 'mysecretkey'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
    #initialize jwt manager
    jwt = JWTManager(app)
    app.config.from_object(app_config[config_name])
    #initialize db
    init_db()

    from .v1.endpoints import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    from .v2.endpoints import api2 as api2_blueprint
    app.register_blueprint(api2_blueprint, url_prefix='/api/v2')
    
    return app
  
