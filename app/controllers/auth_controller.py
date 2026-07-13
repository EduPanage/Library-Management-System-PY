from app.services.auth_service import AuthService

class AuthController:

    def __init__(self, db):
        self.auth_service = AuthService(db)

    def register(self):
        print("\n\n=== User Register ===")

        nome = input("\nName: ")
        email = input("Email: ")
        password = input("Password: ")
        perfil = input("Profile: (ADMIN/EMPLOYEE/CLIENT): ").upper()

        try: 
            self.auth_service.register(
                nome,
                email,
                password,
                perfil
            )

            print("\nSuccess: User Registered!")

        except Exception as error:
            print(f"\nError: {error}")

    def login(self):

        print("\n=== Login ===")

        email = input("\nInsert your email: ")
        password = input("Insert your password: ")

        try:
            usuario = self.auth_service.login(email, password)

            print(f"\nWelcome, {usuario.nome}")
            print(f"Perfil: {usuario.perfil}")

            return usuario
        
        except Exception as error:
            print(f"\nError: {error}")
            return None