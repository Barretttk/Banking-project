# <-- install - "pipenv install flask pymysql flask-bcrypt 

from flask_app import app

#======================================
# controllers has to match controllers can have multi   example dojos_controllers, Ninjs_controllers 
#======================================

from flask_app.controllers import controller_account_types, controller_defaults, controller_users_log, controller_users_reg, controller_invest







if __name__ == "__main__":
    app.run(debug=True)