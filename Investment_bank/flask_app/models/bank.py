from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE



class Bank:

    def __init__(self, data):

        self.id = data['id']
        self.name = data["name"]
        self.checking_account = data["checking"]
        self.saving_account = data["saving"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]