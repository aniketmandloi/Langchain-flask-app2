from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aniketmandloi'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#Whatever1234567@localhost/langchainDB'
app.config['OPENAI_API_KEY'] = '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'
db = SQLAlchemy(app)

from app import routes, models