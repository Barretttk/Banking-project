from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#==================================
#import models from models folder
#==================================

from flask_app.models.model_user import User




#=================== Registration Page ========================

@app.route("/Accent_Empire/registration")
def registration():
    return render_template("account_registration")


#================  Registration  =================

@app.route("/Accent_Empire/registration", methods=['POST'])
def process_registration():
    # validate

    if not model_user.User.validate_registration(request.form):
        return redirect("/")

    # Verify user already exists

    user_exists = model_user.User.get_one_by_email(request.form)
    if user_exists == True:
        flash("This Emails already exsist. ", "err_reg_email")
        return redirect("/")

    #hash  
    hash_password = bcrypt.generate_password_hash(request.form['password'])

    #create
    data = {
        **request.form,
        'password' : hash_password
    }
    user_id = model_user.User.create(data)

    #store ID into session
    session["first_name"] = data["first_name"]
    session["email"] = data["email"]
    session["uuid"] = user_id

    return redirect("/dashboard")
