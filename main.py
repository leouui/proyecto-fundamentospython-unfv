from helpers import optionsShow,clearConsole
from pages.Login import Login
from pages.Register import RegisterUser
from pages.App import App
from database.actions import addUser


while True:
    optionsShow("---------Bienvenido al programa---------", 
                "Iniciar Sesion",
                "Registrarse",
                "Salir")
    try:
        option = int(input("Escoja una opcion: "))
        clearConsole()
    except ValueError:
        option=0
        clearConsole()
    
    print("Test")
    match option:
        case 1:
            user = Login()
            if(not(user is None)): App(user)
        case 2:
            user = RegisterUser()
            if(not(user is None)): addUser(user)
        case 3:
            break
        case 0:
            print("ERROR: Ingrese un número válido (1, 2, o 3).")
            input("Presione ENTER para continuar.")
        case _:
            print("Ingrese una opcion correcta")



