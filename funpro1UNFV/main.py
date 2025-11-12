from helpers import optionsShow,clearConsole
from pages.Login import Login
from pages.Register import RegisterUser
from pages.App import App
from database.actions import addUser

while True:
    optionsShow("---------Bienvenido al programa---------", "Iniciar Sesion", "Registrarse","Salir")
    option = int(input("Escoja una opcion: "))
    clearConsole()
    
    match option:
        case 1:
            user = Login()
            if(not(user is None)): 
                App(user)
        case 2:
            user = RegisterUser()
            if(not(user is None)): 
                addUser(user)
        case 3:
            break
        case __:
            print("Ingrese una opcion correcta")
            print("majo no chambea......")