from flask import Flask
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE')
db_host = os.environ.get('CLOUD_SQL_HOST')
db_port = os.environ.get('CLOUD_SQL_PORT')

app = Flask(__name__)

def create_app(test_config=None):

    db_url = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}' 

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    
    db.init_app(app)
    migrate.init_app(app, db)

    engine = db.create_engine(db_url, {})

    conn = engine.connect()
    
    # from app.model.gcs import GCS

    from .routes import image_bp
    app.register_blueprint(image_bp)

    CORS(app)

    return app

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))