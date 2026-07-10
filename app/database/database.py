import os
import psycopg
from dotenv import load_dotenv

class Database:
        
    def __init__(self):
        
        load_dotenv()
        
        self.host = os.getenv("DB_HOST")
        self.port = int(os.getenv("DB_PORT"))
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        
        self.connection = None

    
    def conect (self):
        
        try: 
            self.connection = psycopg.connect(
                host=self.host,
                port=self.port,
                dbname=self.database,
                user=self.user,
                password=self.password
            )
            
            print("\n\nSuccess: Connected to the Database!")
            print(f"DB Name: {self.database} \nPort: {self.port}\n\n")
            
        except Exception as erro:
            print(f"\n\nError: Failed to connect to the Database ({erro})!\n\n")

    def fechar(self):
        
        if self.connection:
            self.connection.close()
            print("Connection closed\n\n")

