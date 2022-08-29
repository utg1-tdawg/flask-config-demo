import os
from flask import Flask
from public_config import DevelopmentConfig


app = Flask(__name__)

#####################################
### Configuring from python files ###
#####################################

# Method 1: from_pyfile
app.config.from_pyfile("public_config_dev.py")
print("Method 1", app.config.get("CONFIG"))


# Method 2: from_object
app.config.from_object(DevelopmentConfig)
print("Method 2", app.config.get("CONFIG"))
print("Method 2", app.config.get("DEV_CONFIG"))


##############################################
### Configuring from environment variables ###
##############################################

### Method 3: from_prefixed_env
# Reads environment variables that begin with FLASK_
app.config.from_prefixed_env()
print("Method 3", app.config.get("DEMOMO"))

### Method 4: from .env file
from dotenv import load_dotenv

load_dotenv()
print("Method 4", os.environ.get("FLASK_FROM_ENV"))
