from app.database.database import Database

def main():
    db = Database()
    
    db.connect()
    db.close()
    
    
if __name__ == "__main__":
    main()