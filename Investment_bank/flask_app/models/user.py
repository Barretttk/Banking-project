from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE



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

#     @classmethod
#     def