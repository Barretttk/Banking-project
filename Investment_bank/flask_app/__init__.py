from flask import Flask

app = Flask(__name__)

#================================
# From what data base - ie schema
#================================

DATABASE = "bank_schema"

app.secret_key = "ofghsgogdoigsdikn"