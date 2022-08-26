from flask import Flask
import re
from flask_bcrypt import Bcrypt



app = Flask(__name__)

app.secret_key = "ofghsgogdoigsdikn"


#================================
# From what data base - ie schema
#================================

DATABASE = "bank_schema"


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

bcrypt = Bcrypt(app)