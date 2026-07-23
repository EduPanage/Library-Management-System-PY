from app.models.autor import Autor
from app.repositories.autor_repository import AutorRepository

class AutorService:

    def __init__(self, db):
        self.autor_repository = AutorRepository(db)

    def register (self, nome):

        nome = nome.strip()

        if not nome:
            raise ValueError("Author name cannot be empty!")

        autor = Autor(nome=nome)

        self.autor_repository.save(autor)


    def list_authors(self):
        return self.autor_repository.list_authors()


    def search_by_id(self, id):

        autor = self.autor_repository.search_by_id(id)

        if autor is None:
            raise ValueError("Author not found.")

        return autor


    def update(self, id, nome):

        autor = self.search_by_id(id)

        nome = nome.strip()

        if not nome:
            raise ValueError("Author name cannot be empty.")

        autor.nome = nome

        self.autor_repository.update(autor)


    def delete(self, id):

        self.search_by_id(id)

        self.autor_repository.delete(id)