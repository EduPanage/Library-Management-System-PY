from app.database.database import Database
from app.controllers.menu_controller import MenuController

def main():
    db = Database()
    db.connect()

    menu_controller = MenuController(db)

    menu_controller.start()

    db.close()
    
    
if __name__ == "__main__":
    main()