from database.users import users
from helpers import SearchUserByName, optionsShow

def RegisterUser():
    print("---------Registro---------")
    
    while True:
        userName = input("Ingrese el nombre del usuario: ")
        result = SearchUserByName(userName,users)
    
        if(result[0]):
            optionsShow("---El usuario ya existe","Volver al Inicio","Ingresar el nombre de usuario nuevamente:")
            
            match int(input("Escoja una opcion: ")):
                case 1: return
                case 2: continue
        
        password = input("Ingrese la contrasenia: ")
        
        if(len(password)<6):
            optionsShow("---La contraseña debe tener al menos 7 caracteres", "Volver al Inicio","Ingresar la contraseña nuevamente:" )

            match int(input("Escoja una opcion: ")):
                case 1: return
                case 2: continue
        
        optionsShow("---Registro satisfactorio!!","Volver")
        input("Escoja una opcion: ")

        return {
            "name":userName,
            "password":password
        }