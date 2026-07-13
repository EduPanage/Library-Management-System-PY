from app.database.database import Database
from app.controllers.auth_controller import AuthController

def main():
    db = Database()
    db.connect()

    auth_controller = AuthController(db)

    auth_controller.register()

    db.close()
    
    
if __name__ == "__main__":
    main()