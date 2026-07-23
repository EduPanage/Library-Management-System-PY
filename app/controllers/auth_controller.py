from app.services.auth_service import AuthService

class AuthController:

    def __init__(self, db):
        self.auth_service = AuthService(db)

    def menu(self):

        while True:

            print("\n===== Library Management System =====")
            print("\n1 - Login")
            print("2 - Register")
            print("0 - Exit") 

            option = input("\nOption: ")

            match option:

                case "1":
                    usuario = self.login()

                    if usuario:
                        return usuario

                case "2":
                    usuario = self.register()

                case "0":
                    print("\nExiting the system!")
                    return None

                case _:
                    print("\nInvalid option, choose again!")

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