from app.database.database import Database
from app.controllers.auth_controller import AuthController

def main():
    db = Database()
    db.connect()

    auth_controller = AuthController(db)

    usuario = auth_controller.menu()

    db.close()
    
    
if __name__ == "__main__":
    main()