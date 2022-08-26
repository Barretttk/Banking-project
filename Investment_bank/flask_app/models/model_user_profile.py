from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app import EMAIL_REGEX

from flask import flash, session



class User_profile:

    def __init__(self, data):
        self.id = data['id']

        self.address = data["address_1"]

        self.city = data["city"]

        self.state = data["state"] #2 characters

        self.zip_code = data["zip_code_"]
        
        self.birth_date = data["birth_date"]  #month / day / year

        self.phone = data["phone"] ### - ### - ####


        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

               #============================================