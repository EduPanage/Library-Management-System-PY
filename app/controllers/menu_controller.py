from app.controllers.auth_controller import AuthController
from app.utils.terminal_function import sleep, clear_terminal


class MenuController:

    def __init__ (self, db):
        self.auth_controller = AuthController(db)

    def start(self):

        while True:
        
                print("\n===== Library Management System =====")
                print("\n1 - Login")
                print("2 - Register")
                print("0 - Exit") 
        
                option = input("\nOption: ")
        
                match option:
        
                    case "1":
                        usuario = self.auth_controller.login()
        
                        if usuario:
                            self.show_home(usuario)
        
                    case "2":
                        usuario = self.auth_controller.register()
        
                    case "0":
                        print("\nExiting the system!")
                        return
        
                    case _:
                        print("\nInvalid option, choose again!")


    def show_home(self, usuario):

        while True:

            print("\n==========================")
            print(f"Welcome, {usuario.nome}")
            print(f"Profile: {usuario.perfil}")
            print("==========================")

            if usuario.perfil == "ADMIN":
                sleep()
                clear_terminal()
                self.admin_menu()

            elif usuario.perfil == "EMPLOYEE":
                sleep()
                clear_terminal()
                self.employee_menu()

            elif usuario.perfil == "CLIENT":
                sleep()
                clear_terminal()
                self.client_menu()

            break


    def admin_menu(self):

        print("\n===== ADMIN MENU =====")
        print("\n1 - Manage Users")
        print("2 - Manage Books")
        print("3 - Manage Authors")
        print("4 - Manage Categories")
        print("5 - Reports")
        print("0 - Logout")

        input("\nPress ENTER to logout...")



    def employee_menu(self):

        print("\n===== EMPLOYEE MENU =====")
        print("\n1 - Books")
        print("2 - Loans")
        print("3 - Returns")
        print("0 - Logout")

        input("\nPress ENTER to logout...")



    def client_menu(self):

        print("\n===== CUSTOMER MENU =====")
        print("\n1 - Search Books")
        print("2 - My Loans")
        print("3 - Rent Book")
        print("4 - Return Book")
        print("0 - Logout")

        input("\nPress ENTER to logout...")