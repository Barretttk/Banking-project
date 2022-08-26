from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#==================================
#import models from models folder
#==================================

from flask_app.models.model_user import User





# ================== default routes ===============

@app.route("/")
def index():
    # if "uuid" in session:
    #     return redirect("/dashboard")
    return render_template("log_reg.html")

@app.route("/Accent_Empire/dashboard")
def dashboard():
    # if "uuid" not in session:
    #     return redirect("/")


    return render_template("dashboard.html")



# @app.route('/<path:path>')
# def catch_all(path):
#         return 'page not found'


