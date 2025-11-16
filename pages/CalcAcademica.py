from helpers import clearConsole,optionsShow
Notas={}

def AgregarMateria(user):
    if user not in Notas:
       Notas[user]={"Materias":{}}
    mat=input("Ingrese el nombre de la materia: ").upper()
    if mat not in Notas[user]["Materias"]:
        Notas[user]["Materias"][mat]=[]
        optionsShow("Materia Agregada","Agregar otra materia","Regresar")
    else:
        optionsShow("La materia ya existe","Agregar otra materia","Regresar")
    op=input("Ingrese una opcion: ")
    clearConsole()
    match op:
        case "1":
            AgregarMateria(user)
        case "2":
            return
        case _:
            input("Opcion no valida\nRegresar[ENTER]")
            return

def printMateria(user):
    print("--------MATERIAS---------")
    for i,e in enumerate(Notas[user]["Materias"],0):
        print(i+1,e)
    print("-------------------------")
    return ([n for n in Notas[user]["Materias"]])

def AgregarNota(user):
    clearConsole()
    materias=printMateria(user)
    try :
        mat=(int(input("Elija una materia para agregar notas:"))-1)
    except ValueError:
        clearConsole()
        input("ERROR ingrese el numero de la materia\nRegresar[ENTER]")
        AgregarNota(user)
        return
    clearConsole()
    if mat>(len(materias)-1) or mat<0:
        input("ERROR materia no encontrada\nRegresar[ENTER]")
        AgregarNota(user)
        return
    while True:
        while True:
            clearConsole()
            print(f"Ha seleccionado: {materias[mat]}")
            try:
                nota=float(input("Ingrese la nota: "))
                peso=float(input("Ingrese el peso de la nota: "))
                break
            except ValueError:
                clearConsole()
                op=input("Valores no validos\nRegresar[ENTER]")
        Notas[user]["Materias"][materias[mat]].append({"nota":nota,"peso":peso})
        optionsShow("Se agregado correctamente","Agregar otra nota","Regresar")
        op=input("Ingrese una opcion: ")
        match op:
            case "1":
                continue
            case "2":
                return
            case _:
                input("Opcion no valida\nRegresar[ENTER]")
                continue

def VerMaterias(user):
    if user not in Notas:
        print("No hay notas registradas")
        input("Regresar [ENTER]")
        return
    printMateria(user)
    print("Opciones\nAgregar una materia [1]\nRegistrar nota [2]\nRegresar [3]")
    op = input("Ingrese una opcion")
    clearConsole()
    match op:
        case "1":
            AgregarMateria(user)
        case "2":
            AgregarNota(user)
        case "3":
            return
        case _:
            input("Opcion no valida\nRegresar[ENTER]")
            clearConsole()
            VerMaterias(user)
            return

def CalcPromedio(user):
    clearConsole()
    if user not in Notas:
        print("No hay notas registradas")
        input("Regresar [ENTER]")
    materias=printMateria(user)
    try:
        i=int(input("Ingrese el la materia a calcular el promedio: "))-1
    except ValueError:
        input("ERROR ingrese un numero valido\nRegresar[ENTER]")
        CalcPromedio(user)
        return
    clearConsole()
    if i>len(materias) or i < 0:
        input("No se encontro la materia\nRegresar[ENTER]")
    nota_user=Notas[user]["Materias"][materias[i]]
    if not nota_user:
        input("No hay notas registradas\nRegresar[ENTER]")
        return
    suma=0
    peso_total=0
    for n in nota_user:
        print(n["nota"],n["peso"])
        suma+=n["nota"]*(n["peso"]/100)
        peso_total+=n["peso"]
    print("El promedio ponderado es ",suma)
    input("Regresar[ENTER]")

def CalcAcademica(user):
    while True:
        optionsShow(f"{user} Bienvenid@ a la calculadora de notas ",
                    "Agregar una materia",
                    "Registrar nota",
                    "Ver materias",
                    "Calcular promedio",
                    "Salir")
        op=input("Ingrese una opcion: ")
        clearConsole()
        match op:
            case "1":
                AgregarMateria(user)
            case "2":
                AgregarNota(user)
            case "3":
                VerMaterias(user)
            case "4":
                CalcPromedio(user)
            case "5":
                return
            case _:
                print("Opcion no valida")
                input("Rintentar[ENTER]")

if __name__=="__main__":
    CalcAcademica(user="Anto")