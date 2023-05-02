from flask import Flask, request
# from flask_cors import CORS
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

# CORS(app, origins = ["*"])

migrate = Migrate(app, db)
db.init_app(app)

if __name__ == "__main__":
    app.run(port=3001, debug=True)