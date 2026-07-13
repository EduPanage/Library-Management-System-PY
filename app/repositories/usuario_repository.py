from database.database import Database

class UsuarioRepository:
    

    def __init__(self):
        self.db = Database()
        self.db.connect()

    def save(self, usuario):
        query = """
            INSERT INTO usuarios (nome,
                                  email,
                                  senha_hash,
                                 perfil,
                                ativo
                                 )
            VALUES (%s, %s, %s, %s, %s)
         """
    
        with self.db.connection.cursor() as cursor:
             cursor.execute(
                  query,
                  (
                      usuario.nome, 
                      usuario.email,
                      usuario.senha_hash,
                     usuario.perfil,
                      usuario.ativo
                 )
             )

        self.db.connection.commit()

    def search_by_email (self, email):
        query = """
            SELECT *
            FROM usuarios
            WHERE email = %s
        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(query, (email,))
            return cursor.fetchone()
        
    def listUsers (self):

        query = """
            SELECT *
            FROM usuarios
            ORDER BY nome
        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        
    def close (self):
        self.db.close()



















