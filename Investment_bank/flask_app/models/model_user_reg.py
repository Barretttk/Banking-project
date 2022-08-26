from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app import EMAIL_REGEX

from flask import flash, session



# =================  REG VALIDATE  ===========================

    @staticmethod
    def validate_registration(data:dict) -> bool:
        query = "Select * From users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)

        is_valid = True # we assume this is true

        if len(data['first_name']) < 3:
            flash("First name min  characters.", 'err_reg_first_name')
            is_valid = False

        if len(data['last_name']) < 3:
            flash("Last name min 3 characters.", 'err_reg_last_name')
            is_valid = False

        if len(data['email']) < 1:
            is_valid = False
            flash("Field is required.", 'err_reg_email')
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email!", 'err_reg_email')
            is_valid = False
        else:
            # check db to see if email already exist
            existing_user = User.get_one_by_email({'email' : data['email']})
            if existing_user:
                flash("User already exist!", 'err_reg_email')
                is_valid = False
        if len (results) >= 1:
            flash("User already exist!", 'err_reg_email')
            is_valid = False

        if len(data['password']) < 8:
            flash("password min 8 characters.", 'err_reg_password')
            is_valid = False

        if len(data['confirm_pw']) < 8:
            flash("Field is reqired.", 'err_reg_confirm_pw')
            is_valid = False
        elif data['password'] != data['confirm_pw']:
            is_valid = False
            flash("Passwords do not match", 'err_reg_confirm_pw')

        return is_valid
