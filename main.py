from app.database.database import Database

def main():
    db = Database()
    
    db.conectar()
    db.fechar()
    
    
if __name__ == "__main__":
    main()