from helpers import clearConsole,optionsShow,SearchUserByAtr,continueUntilCorrect
from database.actions import modifyDataUser
from .validations.CalcAcademica import courseTitlevalidation
from database.users import users
# el codigo falla cuando se intenta con varios usuarios, la idea de definir un objeto global no funciona, para eso puedes guiarte de lo que hice en apuntes, y en lugar de ser {"username":...,"usercode":..., "password":...,"notes":[],"Materias":{...}}
# debe ser {"username":...,"usercode":..., "password":...,"notes":[],"courses":{...}} pq debe ser uniformemente en ingles 
# basate en el codigo que te corregi de apuntes para implementar tu solucion, y utiliza la funcion continueUntilIsCorrect que esta en helpers, las validaciones tienes que crearlas especificamente en la capreta validations(Hay ejemplos de que formato deben tener)
# igual puedes preguntarme

def AgregarMateria(materias,user):
    mat=continueUntilCorrect("Ingrese el nombre de la materia: ",courseTitlevalidation).upper()
    if mat not in materias:
        #En este metodo se agrega una nueva materia al diccionario de materias del usuario actual
        #con la estructura {"grades":[],"prom":[]}
        #en grades se almacenaran las notas como diccionarios {"nota":valor,"peso":valor}
        materias[mat]={"grades":[],"prom":[]}
        modifyDataUser(user["usercode"],{**user,"courses":materias})
        optionsShow("Materia Agregada")
    else:
        print("La materia ya existe")
    input("Regresar [ENTER]")
    clearConsole()
#este metodo solo imprime las materias disponibles
def printMateria(materias):
    print("--------MATERIAS---------")
    for i,e in enumerate(materias,0):
        print(i+1,e)
    print("-------------------------")
#este metodo permite seleccionar una materia de la lista de materias disponibles
def selectMat(materias):
    while True:
        printMateria(materias)
        try :
            mat=(int(input("Seleccione una materia: "))-1)
            if mat>(len(materias)-1) or mat<0:
                clearConsole()
                input("ERROR materia no encontrada\nRegresar[ENTER]")
            else:
                seleccion=[n for n in materias]
                materia=seleccion[mat]
                return materia
        except ValueError:
            clearConsole()
            input("ERROR Valor no valido\nRegresar[ENTER]")
        clearConsole()
#este metodo agrega una nota a la materia seleccionada
#nota es un diccionario {"nota":valor,"peso":valor}
def AgregarNota(materias,user):
    if not materias:
        print("No hay materias registradas")
        input("Regresar [ENTER]")
        return
    while True:
        clearConsole()
        materia=selectMat(materias)
        break
    while True:
        while True:
            clearConsole()
            print(f"Ha seleccionado: {materia}")
            try:
                nota=float(input("Ingrese la nota: "))
                peso=float(input("Ingrese el peso de la nota %: "))
                break
            except ValueError:
                clearConsole()
                op=input("Valores no validos\nRegresar[ENTER]")
        materias[materia]["grades"].append({"nota":nota,"peso":peso})
        optionsShow("Se agregado correctamente","Agregar otra nota","Regresar")
        op=input("Ingrese una opcion: ")
        match op:
            case "1":
                continue
            case "2":
                modifyDataUser(user["usercode"],{**user,"courses":materias})
                return
            case _:
                input("Opcion no valida\nRegresar[ENTER]")
                continue
   
def VerMaterias(materias,user):
    if not materias:
        print("No hay materias registradas")
        input("Regresar [ENTER]")
        return
    print("--------MATERIAS---------")
    for i,e in enumerate(materias,0):
        print(i+1,e)
        notas_user=materias[e]["grades"]
        if notas_user:
            print("    Notas Registradas:")
            for i,n in enumerate(notas_user,1):
                print(f"    {i}. Nota: {n["nota"]} Peso: {n["peso"]}%")
    print("-------------------------")
    print("Opciones\nAgregar una materia [1]\nEliminar materia [2]\nAgregar nota [3]\nRegresar [4]")
    op = input("Ingrese una opcion: ")
    clearConsole()
    match op:
        case "1":
            AgregarMateria(materias,user)
        case "2":
            EliminarMateria(materias,user)
        case "3":
            AgregarNota(materias,user)
        case "4":
            return    
        case _:
            input("Opcion no valida\nRegresar[ENTER]")
            clearConsole()
            return

def CalcPromedio(materias,user):
    clearConsole()
    if not materias:
        print("No hay notas registradas")
        input("Regresar [ENTER]")
        return
    materia=selectMat(materias)
    notas_user=materias[materia]["grades"]
    clearConsole()
    if not notas_user:
        input("No hay notas registradas\nRegresar[ENTER]")
        return
    suma=0
    peso_total=0
    #print(notas_user)
    for n in notas_user:
        print(f"Nota: {n["nota"]} Peso: {n["peso"]}%")
        suma+=n["nota"]*(n["peso"]/100)
        peso_total+=n["peso"]
    if peso_total!=100:
        print(f"El peso total de las notas es {peso_total}%")
    suma=round(suma,2)
    materias[materia]["prom"].append(suma)
    modifyDataUser(user["usercode"],{**user,"courses":materias})
    print("El promedio ponderado es ",suma)
    input("Regresar[ENTER]")

def EliminarMateria(materias, user):
    clearConsole()
    if not materias:
        print("No hay materias para eliminar")
        input("Regresar [ENTER]")
        return
    print("Materias disponibles para eliminar:")
    materia = selectMat(materias)
    clearConsole()
    while True:
        optionsShow(f"Confirme eliminación de: {materia}", "Eliminar", "Cancelar")
        op = input("Ingrese una opcion: ")
        clearConsole()
        match op:
            case "1":
                del materias[materia]
                modifyDataUser(user["usercode"], {**user, "courses": materias})
                optionsShow("Materia eliminada")
                input("Regresar [ENTER]")
                clearConsole()
                return
            case "2":
                input("Eliminacion cancelada\nRegresar[ENTER]")
                return
            case _:
                input("Opcion no valida\nRegresar[ENTER]")
                clearConsole()

def MenuCalculadora(user):
#muestra la calculadora academica para el usuario dado, permitiendole gestionar materias, notas y calcular promedios.
    while True:
        materias = SearchUserByAtr("usercode", user["usercode"], users)[1]["courses"]
        optionsShow(f"{user['username']} Bienvenid@ a la calculadora de notas ",
                    "Agregar una materia",
                    "Registrar nota",
                    "Ver materias",
                    "Calcular promedio",
                    "Eliminar materia",
                    "Salir")
        # print(materias) 
        # print(user)
        op=input("Ingrese una opcion: ")
        clearConsole()
        match op:
            case "1":
                AgregarMateria(materias,user)
            case "2":
                AgregarNota(materias,user)
            case "3":
                VerMaterias(materias,user)
            case "4":
                CalcPromedio(materias,user)
            case "5":
                EliminarMateria(materias,user)
            case "6":
                return
            case _:
                print("Opcion no valida")
                input("Reintentar[ENTER]")