from app.services.auth_service import AuthService

class AuthController:

    def __init__(self, db):
        self.auth_service = AuthService(db)

    def register(self):
        print("\n\n===User Register===")

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
            print(f"Error: {error}")