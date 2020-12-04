from flask import Flask
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

client = MongoClient('mongodb://localhost:27017/')
db = client['EcoFoto']


bcrypt = Bcrypt(app)



from app.routes import routes
