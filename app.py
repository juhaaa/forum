from flask import Flask
from os import getenv

# Initialize flask app

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SESSION_PERMANENT"] = False

# Import routes module

import routes
