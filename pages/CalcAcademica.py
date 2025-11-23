from helpers import clearConsole,optionsShow,SearchUserByAtr,dynamicInputs
from database.actions import modifyDataUser
from .validations.CalcAcademica import courseTitlevalidation,selectCoursevalidation,floatValidation
from database.users import users

def listarMaterias(materias,det=False):
    l="--------MATERIAS---------\n"
    for i,e in enumerate(materias): 
        l+=f"{i+1}) {e}\n"
        if not(det): continue
        
        notas_user=materias[e]["grades"]
        if not(notas_user): continue
        
        l+="    Notas Registradas:\n"
        for i,n in enumerate(notas_user,1):
            l += f"    {i}. Nota: {n['nota']} Peso: {n['peso']}%\n"

    l+="-------------------------"
    
    return l

def selectMat(materias):
    while True:
        results = dynamicInputs(listarMaterias(materias),
            ["Seleccione una materia: ",selectCoursevalidation,materias] # results 0
        )
        if results is None: return None

        seleccion=[n for n in materias]
        return seleccion[results[0]-1]

def AgregarMateria(materias,user):
    results = dynamicInputs("----Agregar Materia----",
        ["Ingrese el nombre de la materia: ",courseTitlevalidation,materias] # results[0]
    )
    if results is None: return
 
    materias[results[0]]={"grades":[]}
    modifyDataUser(user["usercode"],{**user,"courses":materias})

    input("--> Materia Agregada con exito\nRegresar[Enter] ")

def AgregarNota(materias,user):
    if not materias:
        return input("--> No hay materias registradas\nRegresar [ENTER] ")
    
    materia=selectMat(materias)
    if materia is None: return

    results = dynamicInputs(f"--> Ha seleccionado el curso: {materia}",
        ["Ingrese la nota: ",floatValidation], # results[0]
        ["Ingrese el peso de la nota %: ",floatValidation] # results[1]
    )

    if results is None: return

    materias[materia]["grades"].append({"nota":results[0],"peso":results[1]})
    modifyDataUser(user["usercode"],{**user,"courses":materias})
    
    input("--> Se agrego la nota correctamente\nRegresar[ENTER] ")

def EliminarMateria(materias, user):
    if not materias:
        return input("--> No hay materias para eliminar\nRegresar [ENTER] ")
    
    print("Materias disponibles para eliminar:")
    materia = selectMat(materias)
    if materia is None: return

    while True:
        optionsShow(f"Confirme eliminación de: {materia}", "Eliminar", "Cancelar")
        op = input("Ingrese una opcion: ")

        if(op != "1"): return input("--> Eliminacion cancelada\nRegresar[ENTER] ")

        del materias[materia]
        modifyDataUser(user["usercode"], {**user, "courses": materias})

        return input("--> Materia eliminada\nRegresar [ENTER] ")

def VerMaterias(materias):
    if not materias:
        return input("--> No hay materias registradas\nRegresar [ENTER] ")
    
    print(listarMaterias(materias,True))
    input("Regresar [Enter] ")

def CalcPromedio(materias):
    if not materias:
        return input("--> No hay materias registradas\nRegresar [ENTER]")
    
    materia = selectMat(materias)
    if materia is None: return

    notas_user=materias[materia]["grades"]
    if not notas_user:
        return input("--> No hay notas registradas\nRegresar [ENTER]")
    
    print(f"--> Ha seleccionado el curso: {materia}")
    suma, peso_total = 0 ,0
    for n in notas_user:
        print(f"--> Nota: {n['nota']} Peso: {n['peso']}%")
        suma+=n["nota"]*(n["peso"]/100)
        peso_total+=n["peso"]

    if peso_total!=100: print(f"    El peso total de las notas es {peso_total}%")

    input(f"    El promedio ponderado es: {round(suma,2)}\nRegresar[ENTER] ")

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
            case "1": AgregarMateria(materias,user)
            case "2": AgregarNota(materias,user)
            case "3": VerMaterias(materias)
            case "4": CalcPromedio(materias)
            case "5": EliminarMateria(materias,user)
            case "6": break
            case _: input("-->Ingrese una opcion valida\nContinuar[ENTER] ")