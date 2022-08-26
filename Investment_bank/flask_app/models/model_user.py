from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app import EMAIL_REGEX

from flask import flash, session



class User:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]

        self.password = data["password"] # min 8 characters, 1 Number, 1 special character
        self.password_confirmation = data["password_confirmation"]

        self.address_1 = data["address_1"]
        self.address_2= data["address_2"]
        
        self.city = data["city"]
        self.state = data["state"] #2 characters

        self.zip_code = data["zip_code_"]
        self.country = data["country"]

        self.phone = data["phone"] ### - ### - ####

        self.birth_date = data["birth_date"]  #month / day / year

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        #============================================

#     @classmethod
#     def

#=======================  LOGIN VALIDATE  ======================

    # @staticmethod
    # def validate_login(data:dict) -> bool:
    #     is_valid = True # we assume this is true

    #     if len(data['email']) < 1:
    #         is_valid = False
    #         flash("Field is required")
    #     elif not EMAIL_REGEX.match(data['email']):
    #         flash("Invalid email address!", 'err_user_email_login')
    #         is_valid = False
    #     else:
    #         #cheeck db to see if email already exist
    #         existing_user = User.get_one_by_email({'email' : data['email']})
    #         if not existing_user:
    #             flash("Email not found!", 'err_user_email_login')
    #             is_valid = False

    #     if len(data['password']) < 8:
    #         flash("Field is reqired")
    #         is_valid = False

    #     if is_valid:
    #         # check bcrypt
    #         if not bcrypt.check_password_hash(existing_user.password, data["password"]):
    #             flash("Invalid Credentials!", 'err_user_password_login')
    #             is_valid = False

    #             #get the id into seaion
    #             session['user_id'] = existing_user.id

    #     return is_valid



    # @staticmethod
    # def validate_user(data:dict) -> bool:
    #     query = "Select * From users WHERE email = %(email)s;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)

    #     is_valid = True # we assume this is true

    #     if len(data['first_name']) < 3:
    #         flash("First name min  characters.", 'err_reg_first_name')
    #         is_valid = False

    #     if len(data['last_name']) < 3:
    #         flash("Last name min 3 characters.", 'err_reg_last_name')
    #         is_valid = False

    #     if len(data['email']) < 1:
    #         is_valid = False
    #         flash("Field is required.", 'err_reg_email')
    #     elif not EMAIL_REGEX.match(data['email']):
    #         flash("Invalid email!", 'err_reg_email')
    #         is_valid = False

    #     return is_valid