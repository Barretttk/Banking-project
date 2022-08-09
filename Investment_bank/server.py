
from flask_app import app

#======================================
# controllers has to match controllers can have multi   example dojos_controllers, Ninjs_controllers 
#======================================

from flask_app.controllers import login_controllers, bank_controllers, home_controllers








if __name__ == "__main__":
    app.run(debug=True)