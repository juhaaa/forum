from os import getenv
from flask import Flask


# Init flask app

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SESSION_PERMANENT"] = False

# Import routes module after init

import routes
import errors