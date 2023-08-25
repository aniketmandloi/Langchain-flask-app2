from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aniketmandloi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/nameofDB'
app.config['OPENAI_API_KEY'] = 'your_api_key'
db = SQLAlchemy(app)

from app import routes, models
