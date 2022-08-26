from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#==================================
#import models from models folder
#==================================

from flask_app.models.model_user import User

#=============== Investment Profile Page=====================

@app.route("/Accent_Empire/Investment")
def investment():

        # if "uuid" not in session:
    #     return redirect("/")

    return render_template("investment.html")
