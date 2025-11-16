import random
from helpers import clearConsole,optionsShow,continueUntilCorrect,SearchUserByAtr
from .validations.Apuntes import noteTitlevalidation,numNotesvalidation
from database.users import users
from database.actions import modifyDataUser

def listarApuntes(apuntes):
    print("Tus apuntes: ")

    for (i,note) in enumerate(apuntes):
        print(f"{i+1}) {note['title']}")
        print(f"--> {note['content']}")
    print("------------------------")
    
def CrearApunte(user,apuntes):
    optionsShow("----Crea tu apunte----")
    title = continueUntilCorrect("Título del apunte: ",noteTitlevalidation)
    content = continueUntilCorrect("Contenido del apunte: ",noteTitlevalidation)

    apuntes.append({"id": random.randint(100000000,9999999999), "title": title, "content": content})

    modifyDataUser(user["usercode"],{**user,"notes":apuntes})

    print("Apunte guardado.")

def MostrarApuntes(apuntes):
    if not apuntes:
        optionsShow("No tienes apuntes aún", "Regresar")
        return input("Ingrese una opción: ")
    
    listarApuntes(apuntes)

    print("Regresar[1]")
    input("Ingrese una opción: ")

def EliminarApunte(user,apuntes):

    if not apuntes:
        print("No tienes apuntes que eliminar")
        return input("Regresar[ENTER]")
    
    listarApuntes(apuntes)

    num=continueUntilCorrect("Ingrese el numero de apunte que desea eliminar: ",numNotesvalidation,apuntes)
    apuntes.pop(num-1)
    
    modifyDataUser(user["usercode"],{**user,"notes":apuntes})

    print("Apunte eliminado")
    return input("Regresar [ENTER]")
    
def MenuApuntes(user):
    while True:
        optionsShow(f"---------Bienvenido a tus apuntes {user['username']}---------",
                    "Crear un Apunte",
                    "Mostrar sus apuntes",
                    "Eliminar un apunte",
                    "Salir")
        
        op = input("Ingrese una opcion: ")
        clearConsole()

        apuntes = SearchUserByAtr("usercode",user["usercode"],users)[1]["notes"]
        
        match op :
            case "1": CrearApunte(user,apuntes)
            case "2": MostrarApuntes(apuntes)
            case "3": EliminarApunte(user,apuntes)
            case "4": break
            case _:
                print("Ingrese una opcion valida")
                input("Continuar[ENTER]")