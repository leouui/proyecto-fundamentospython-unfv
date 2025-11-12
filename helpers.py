import os
import platform

def SearchUserByAtr(atr,search,users):
    for user in users:
        if(user[atr] == search):
            return (True, user)
    return (False,None)


def clearConsole():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def optionsShow(init,*options):
    clearConsole()
    print(init)
    for (index,msg) in enumerate(options):
        print(f"{msg} [{index + 1}]")

#El formato del las funciones "validations" deben ser de la siguiente manera: Si dentro de esta funcion existe algo que no se cumple entonces debe retornar (False, El mensaje de error)
# En caso todo se cumpla debe retornar (True,El valor del argumento)

def continueUntilCorrect(textInput,validations=lambda a:(True,None),*args):
    inp = ""

    while True:
        inp = input(textInput)
        (correct,msg) = validations(inp,*args)

        if(correct): 
            inp = msg
            break

        optionsShow(f"---{msg}","Volver al Inicio","Reintentar:")

        match int(input("Escoja una opcion: ")):
            case 1: return None
            case 2: continue
            
    return inp