from helpers import SearchUserByName,optionsShow
from database.users import users

def Login():
    print("---------Inicio de sesion---------")

    while True:
        userName = input("Ingrese el nombre del usuario: ")
        (find,user) = SearchUserByName(userName,users)

        if(not(find)):
            optionsShow("---No se encontro el usuario","Volver al Inicio","Ingresar el nombre de usuario nuevamente:")
            
            match int(input("Escoja una opcion: ")):
                case 1: return
                case 2: continue
        
        password = input("Ingrese la contrasenia: ")
        
        if(user["password"] != password):
            optionsShow("---Contrasenia incorrecta", "Volver al Inicio","Ingresar la contrasenia nuevamente:" )

            match int(input("Escoja una opcion: ")):
                case 1: return
                case 2: continue
        
        return user