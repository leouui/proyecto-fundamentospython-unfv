from helpers import clearConsole,optionsShow,SearchUserByAtr,continueUntilCorrect
from database.actions import modifyDataUser
from .validations.CalcAcademica import courseTitlevalidation
from database.users import users

def selectMat(materias):
    while True:
        clearConsole()
        print("--------MATERIAS---------")
        for i,e in enumerate(materias,0): print(f"{i+1}) {e}")
        print("-------------------------")

        try :
            mat=(int(input("Seleccione una materia: ")))
            if mat>(len(materias)) or mat<0:
                optionsShow("--> Materia no encontrada")
                input("Regresar[ENTER] ")
            else:
                seleccion=[n for n in materias]
                materia=seleccion[mat-1]
                return materia
        except:
            optionsShow("--> Materia no encontrada")
            input("Regresar[ENTER] ")

def AgregarMateria(materias,user):
    optionsShow("----Agregar Materia----")

    mat=continueUntilCorrect("Ingrese el nombre de la materia: ",courseTitlevalidation).upper()

    if mat in materias:
        print("La materia ya existe")
        return input("Regresar [ENTER]")
 
    materias[mat]={"grades":[],"prom":[]}
    modifyDataUser(user["usercode"],{**user,"courses":materias})

    print("--> Materia Agregada con exito")
    input("Regresar[Enter] ")

def AgregarNota(materias,user):
    if not materias:
        print("--> No hay materias registradas")
        return input("Regresar [ENTER]")
    
    materia=selectMat(materias)

    while True:
        clearConsole()
        print(f"Ha seleccionado: {materia}")
        try:
            nota=float(input("Ingrese la nota: "))
            peso=float(input("Ingrese el peso de la nota %: "))
            break
        except:
            optionsShow("--> Valores no validos")
            input("Reintentar[ENTER]")

    materias[materia]["grades"].append({"nota":nota,"peso":peso})
    modifyDataUser(user["usercode"],{**user,"courses":materias})

    print("--> Se agrego la nota correctamente")
    return input("Regresar[ENTER] ")

def VerMaterias(materias):
    if not materias:
        print("No hay materias registradas")
        return input("Regresar [ENTER]")
    
    print("--------MATERIAS---------")
    for i,e in enumerate(materias,0):
        print(f"{i+1}) {e}")
        notas_user=materias[e]["grades"]
        if notas_user:
            print("    Notas Registradas:")
            for i,n in enumerate(notas_user,1):
                print(f"    {i}. Nota: {n['nota']} Peso: {n['peso']}%")
    print("-------------------------")
    return input("Regresar [Enter] ")

def CalcPromedio(materias,user):
    if not materias:
        print("-->No hay materias registradas")
        return input("Regresar [ENTER]")
    
    materia=selectMat(materias)
    notas_user=materias[materia]["grades"]
    clearConsole()
    if not notas_user:
        print("-->No hay notas registradas")
        return input("Regresar [ENTER]")
    
    suma=0
    peso_total=0
    for n in notas_user:
        print(f"Nota: {n['nota']} Peso: {n['peso']}%")
        suma+=n["nota"]*(n["peso"]/100)
        peso_total+=n["peso"]
    if peso_total!=100:
        print(f"El peso total de las notas es {peso_total}%")

    suma=round(suma,2)

    materias[materia]["prom"].append(suma)
    modifyDataUser(user["usercode"],{**user,"courses":materias})

    print("El promedio ponderado es: ",suma)
    input("Regresar[ENTER]")

def EliminarMateria(materias, user):
    if not materias:
        print("No hay materias para eliminar")
        return input("Regresar [ENTER]")
    
    print("Materias disponibles para eliminar:")
    materia = selectMat(materias)

    while True:
        optionsShow(f"Confirme eliminación de: {materia}", "Eliminar", "Cancelar")
        op = input("Ingrese una opcion: ")
        clearConsole()
        match op:
            case "1":
                del materias[materia]
                modifyDataUser(user["usercode"], {**user, "courses": materias})
                return input("--> Materia eliminada\nRegresar [ENTER] ")
            case "2":
                return input("--> Eliminacion cancelada\nRegresar[ENTER] ")
            case _:
                input("Opcion no valida\nRegresar[ENTER]")

def MenuCalculadora(user):
    while True:
        optionsShow(f"{user['username']} Bienvenid@ a la calculadora de notas ",
                    "Agregar una materia",
                    "Registrar nota",
                    "Ver materias",
                    "Calcular promedio",
                    "Eliminar materia",
                    "Salir")

        op=input("Ingrese una opcion: ")

        clearConsole()

        materias = SearchUserByAtr("usercode", user["usercode"], users)[1]["courses"]

        match op:
            case "1":
                AgregarMateria(materias,user)
            case "2":
                AgregarNota(materias,user)
            case "3":
                VerMaterias(materias)
            case "4":
                CalcPromedio(materias,user)
            case "5":
                EliminarMateria(materias,user)
            case "6":
                return
            case _:
                print("-->Ingrese una opcion valida")
                input("Continuar[ENTER]")