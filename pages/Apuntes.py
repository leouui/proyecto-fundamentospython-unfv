apuntes=[]
from helpers import clearConsole,optionsShow
def CrearApunte(user):
    clearConsole()
    title = input("Título del apunte: ")
    content = input("Contenido: ")
    apuntes.append({"user": user, "title": title, "content": content})
    print("Apunte guardado.")

def MostrarApuntes(user):
    apuntes_user=[n for n in apuntes if n["user"]==user]
    if not apuntes_user:
        print("No tienes apuntes aún")
        input("Regresar[ENTER]")
        return
    print("Tus apuntes: ")
    i=1
    for note in apuntes_user:
        print(f"{i} {note['title']}")
        print(f"  {note['content']}")
        i+=1

    print("------------------------")
    print("Opciones: \nEliminar un apunte [1]\nRegresar[2]")
    op=input("Ingrese una opción: ")
    clearConsole()
    match op:
        case "1": 
            EliminarApunte(user)
            return
        case "2":
            return
        case _:
            print("Opcion no valida")
            input("Regresar[ENTER]")
            return

def EliminarApunte(user):
    apuntes_user=[n for n in apuntes if n["user"]==user]
    if not apuntes_user:
        print("No tienes apuntes que eliminar")
        input("Regresar[ENTER]")
        return
    print("Tus apuntes: ")
    i=1
    for note in apuntes_user:
        print(f"{i} {note['title']}")
        print(f"  {note['content']}")
        i+=1
    try:
        print("-----------------------------")
        num=int(input("Ingrese el numero de apunte que desea eliminar: "))
        clearConsole()
        if num<1 or num>len(apuntes_user):
            while True:
                print("Opcion invalida\nVolver a intentar [1]\nRegresar [2]")
                op=input("Ingrese una opcion: ")
                clearConsole()
                match op:
                    case "1":
                        EliminarApunte(user)
                        return
                    case "2":
                        return
                    case _:
                        print()
    except ValueError:
        clearConsole()
        while True:
            print("Entrada invalida\nVolver a intentar [1]\nRegresar [2]")
            op=input("Ingrese una opcion: ")
            clearConsole()
            match op:
                case "1":
                    EliminarApunte(user)
                    return
                case "2":
                    return
                case _:
                    input("Opcion invalida\nRegresar[ENTER]")

    for n in apuntes:
        if n is apuntes_user[num-1]:
            apuntes.remove(n)
            print("Apunte eliminado")
            input("Regresar[ENTER]")
            return

def MenuApuntes(user):
    while True:
        optionsShow(f"Bienvenido a tus apuntes {user['username']}","Crear un Apunte","Mostrar sus apuntes","Eliminar un apunte","Salir")
        op=(input("ingrese una opcion: "))
        clearConsole()
        match op :
            case "1":
                CrearApunte(user)
            case "2":
                MostrarApuntes(user)
            case "3":
                EliminarApunte(user)
            case "4":
                break
            case _:
                print("Ingrese una opcion valida")
                input("Continuar[ENTER]")

