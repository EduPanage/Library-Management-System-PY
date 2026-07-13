from app.models.usuario import Usuario

class UsuarioRepository:

    def __init__(self, db):
        self.db = db

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
            result = cursor.fetchone()
        
            if result is None:
                return None
            
            return Usuario(
                id = result[0],
                nome = result[1],
                email=result[2],
                senha_hash=result[3],
                perfil=result[4],
                ativo=result[5],
                criado_em=result[6]

            )
        
    def list_users (self):

        query = """
            SELECT *
            FROM usuarios
            ORDER BY nome
        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        



















