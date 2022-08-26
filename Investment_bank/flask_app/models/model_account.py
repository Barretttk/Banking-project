from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask_app import EMAIL_REGEX

from flask import flash, session


class account_types:

    def __init__(self, data):

        self.id = data['id']
        self.default_int_rate = data["default_int_rate"]
        self.checking_prefex = data["checking_prefex"]
        self.incestment_prefex = data["incestment_prefex"]
        self.saving_prefex = data["saving_prefex"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


        #============================================