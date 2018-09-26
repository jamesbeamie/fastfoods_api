# third-party imports
import os
from flask import Flask

# local imports
from config import app_config
from .dbconect import init_db

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    #initialize database 
    init_db()

    from .v1.orders import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from .v2.orders import api2 as api2_blueprint
    app.register_blueprint(api2_blueprint, url_prefix='/api/v2')
    
    return app
  