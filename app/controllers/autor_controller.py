from app.services.autor_service import AutorService

class AutorController:

    def __init__ (self, db):
        self.autor_service = AutorService(db)

    def register(self):

        print("\n===== REGISTER AUTHOR =====")

        nome = input("\nAuthor name:")

        try:
            self.autor_service.register(nome)
            print("\nAuthor successfully registered!")

        except Exception as e:
            print(f"\nError: {e}")


    def list_authors(self):

        autores = self.autor_service.list_authors()

        print("\n===== AUTHORS =====")

        if not autores:
            print("No authors registered.")
            return

        for autor in autores:
            print(f"{autor.id} - {autor.nome}")


    def update(self):

        id = int(input("Author ID: "))
        nome = input("New name: ")

        try:

            self.autor_service.update(id, nome)

            print("\nAuthor updated successfully!")

        except ValueError as e:

            print(f"\nError: {e}")


    def delete(self):

        id = int(input("Author ID: "))

        try:

            self.autor_service.delete(id)

            print("\nAuthor deleted successfully!")

        except ValueError as e:

            print(f"\nError: {e}")