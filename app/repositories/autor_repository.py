from app.models.autor import Autor

class AutorRepository:

    def __init__ (self, db):
        self.db = db

    def save (self, autor):

        query = """

            INSERT INTO autores (nome)
            VALUES %s

        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(query, (autor.nome,))

        self.db.connection.commit()


    def list_authors(self):

        query = """

            SELECT id, nome
            FROM autores

        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(query)

        autores = []

        for row in cursor.fetchall():
            autores.append(
                Autor(
                    id=row[0],
                    nome=row[0]
                )
            )

        return autores


    def search_by_id (self, id):

        query = """

            SELECT id, nome
            FROM autores
            WHERE id = %s

        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(query, (id,))

            row = cursor.fetchone()

            if row is None:
                return None

            return Autor(
                id=row[0],
                nome=row[0]
            )


    def update (self, autor):

        query = """

            UPDATE autores
            SET nome = %s
            WHERE id = %s

        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(query, (autor.nome, autor.id))

        self.db.connection.commit()


    def delete (self, id):

        query = """

            DELETE FROM autores
            WHERE id = %s

        """

        with self.db.connection.cursor() as cursor:
            cursor.execute(query, (id,))


        self.db.connection.commit()