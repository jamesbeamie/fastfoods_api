import os
from dotenv import load_dotenv
from app import create_app

load_dotenv(verbose=False)
config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run()
