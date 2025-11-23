from helpers import clearConsole,optionsShow,dynamicInputs,SearchUserByAtr
from .validations.Apuntes import noteTitlevalidation,numNotesvalidation
from database.actions import modifyDataUser
from database.users import users

def listarApuntes(apuntes):
    l ="------Tus apuntes------\n"
    for (i,note) in enumerate(apuntes):
        l+= f"{i+1}) {note['title']}\n"
        l+= f"--> {note['content']}\n"
    l +="------------------------"
    return l

def CrearApunte(user,apuntes):
    results = dynamicInputs("----Crea tu apunte----",
        ["Titulo del apunte: ",noteTitlevalidation], # results[0]
        ["Contenido del apunte: ",noteTitlevalidation] # results[1]
    )
    if(results is None): return

    apuntes.append({"title": results[0], "content": results[1]})
    modifyDataUser(user["usercode"],{**user,"notes":apuntes})

    input("--> Apunte guardado\nRegresar[Enter] ")

def MostrarApuntes(apuntes):
    if not apuntes:
        return input("--> No hay apuntes aqui\nRegresar[ENTER] " )
    
    print(listarApuntes(apuntes))
    input("Regresar [Enter] ")

def EliminarApunte(user,apuntes):
    if not apuntes:
        return input("--> No hay apuntes aqui\nRegresar[ENTER] " )

    results = dynamicInputs(listarApuntes(apuntes),
        ["Ingrese el numero de apunte que desea eliminar: ",numNotesvalidation,apuntes] # results[0]
    )

    apuntes.pop(results[0]-1)
    modifyDataUser(user["usercode"],{**user,"notes":apuntes})

    input("--> Apunte eliminado\nRegresar [ENTER] ")
    
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
            case _: input("--> Ingrese una opcion valida\nContinuar[ENTER] ")