from helpers import clearConsole, optionsShow, SearchUserByAtr, dynamicInputs
from .validations.Tareas import tareaTitlevalidation,tareaFechaValidation,numTareaValidation
from database.actions import modifyDataUser
from database.users import users

# Pendientes -> 0
# Completadas -> 1
# Todas -> 2
titulo_vista = ["--- Tareas Pendientes ---","--- Tareas Completadas ---","--- Todas las Tareas ---"]

def obtenerTareas(tareas,filtro=2):
    filtrado = []

    for tarea in tareas:
        if filtro == 0 and not(tarea["completada"]) : filtrado.append(tarea)
        elif filtro == 1 and tarea["completada"]: filtrado.append(tarea)
        elif filtro == 2: filtrado.append(tarea)

    return filtrado

def listarTareas(tareas):
    l = f"{'N°':<3} | {'Fecha Venc.':<12} | {'Estado':<10} | {'Titulo':<25}\n{'-' * 63}"

    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea['completada'] else "Pendiente"
        fecha_str = tarea['fecha_venc']
        l+=f"\n{i+1:<3} | {fecha_str:<12} | {estado:<10} | {tarea['titulo']:<25}"
    l+=f"\n{'-' * 63}" 
    
    return l

def CrearTarea(user, tareas_usuario): 
    results = dynamicInputs("--- Nueva Tarea ---",
        ["Escriba el titulo de la tarea a agregar: ",tareaTitlevalidation], # results[0]
        ["Fecha de vencimiento (formato AAAA-MM-DD) : ",tareaFechaValidation] # results[1]
    )

    if results is None: return

    tareas_usuario.append({ "titulo": results[0], "fecha_venc": results[1], "completada": False })
    modifyDataUser(user["usercode"], {**user, "tasks": tareas_usuario})

    input("--> ¡Tarea creada con éxito!\nRegresar[ENTER] ")

def MostrarTareas(tareas, filtro=2):
    lista_ordenada = sorted(obtenerTareas(tareas,filtro),key=lambda t: t['fecha_venc'])
 
    if not(lista_ordenada):
        return input("--> No hay tareas\nRegresar[ENTER] ")

    print(f"{titulo_vista[filtro]}\n{listarTareas(lista_ordenada)}")
    input("Regresar[ENTER] ")

def MarcarCompletado(user, tareas):
    tareasPendientes = obtenerTareas(tareas,0)

    if not(tareasPendientes):
        return input ("-->No hay tareas pendientes\nRegresar[ENTER] ")
    
    results = dynamicInputs(f"{titulo_vista[0]}\n{listarTareas(tareasPendientes)}",
        ["Ingrese el N° de la tarea a marcar como completada: ",numTareaValidation,tareasPendientes] #results[0]
    )

    if results is None: return

    tareasPendientes[results[0]-1]['completada'] = True 
    modifyDataUser(user["usercode"], {**user, "tasks": tareas})

    input("--> ¡Tarea marcada como completada!\nRegresar[Enter] ")

def EliminarTarea(user, tareas):   
    if tareas is None:
        return input ("-->No hay tareas para eliminar\nRegresar[ENTER] ")
    
    results = dynamicInputs(f"{titulo_vista[0]}\n{listarTareas(tareas)}",
        ["Ingrese el N° de la tarea que desea ELIMINAR.: ",numTareaValidation,tareas] #results[0]
    )
    if results is None: return

    tareas.pop(results[0]-1)
    modifyDataUser(user["usercode"],{**user,"tasks":tareas})
    
    input("--> ¡Tarea eliminada permanentemente!\nRegresar[ENTER] ")

def MenuTareas(user):
    while True:
        optionsShow(f"--- Gestor de Tareas de {user['username'].split()[0]} ---",
                    "Crear Tarea",
                    "Eliminar Tarea",
                    "Marcar Tarea como Completada",
                    "Ver Tareas Pendientes (por fecha)",
                    "Ver Tareas Completadas (Historial)",
                    "Volver al Menú Principal")
        
        opcion = input("Ingrese una opcion: ")
        clearConsole()

        tasksusers = SearchUserByAtr("usercode", user["usercode"], users)[1]["tasks"]

        match opcion:
            case "1": CrearTarea(user, tasksusers)
            case "2": EliminarTarea(user, tasksusers)
            case "3": MarcarCompletado(user, tasksusers)
            case "4": MostrarTareas(tasksusers,filtro=0)
            case "5": MostrarTareas(tasksusers, filtro=1)
            case "6": break 
            case _: input("Opción no válida. Presione ENTER para reintentar.")