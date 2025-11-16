from helpers import clearConsole, optionsShow
import datetime #libreria para manejar fechas y horas

tareas = []

def CrearTarea(usarname):
    """Crear una nueva tarea para el usuario"""
    clearConsole()
    print("--- Nueva Tarea ---")

    titulo = ""
    while not titulo :
        titulo = input("Escriba el tItulo de la tarea a agregar: ")
        if not titulo:
            print("El titulo no puede estar vacío. Intente nuevamente.")

    fecha_valida = None
    while fecha_valida is None:
        fecha_str = input("Fecha de vencimiento (formato AAAA-MM-DD) : ")
        try:
            fecha_valida = datetime.datetime.strftime(fecha_str, '%Y-%m-%d').date()
            if fecha_valida < datetime.date.today():
                print(f"Advertencia: La fecha '{fecha_str}' ya pasó.")
        except ValueError:
            print("Formato de fecha incorrecta. debe de ser AAAA-MM-DD.")

    nueva_tarea = {
        "user": usarname,
        "titulo": titulo,
        "fecha_venc": fecha_valida,
        "completada": False
    }
    tareas.append(nueva_tarea)

    optionsShow("¡Tarea creada con éxito!", "volver")
    input("escoja una opción: ")

def _mostrar_y_obtener_lista(username, filtro='pendientes'):

    clearConsole()

    tareas_usuario = [t for t in tareas if t['user'] == username]
    lista_filtrada = []
    titulo_vista = ""

    if filtro == 'pendientes':
        lista_filtrada = [t for t in tareas_usuario if not t['completada']]
        titulo_vista = "--- Tareas Pendientes (Ordenar por fecha) ---"
    elif filtro == 'completadas':
        lista_filtrada = [t for t in tareas_usuario if t['completada']]
        titulo_vista = "--- Tareas Completadas (Historial) ---"
    elif filtro == 'todas':
        lista_filtrada = tareas_usuario
        titulo_vista = "--- Todas las Tareas (para Eliminar) ---"

    lista_ordenada = sorted(lista_filtrada, key=lambda t: t['fecha_venc'])

    print(titulo_vista)

    if not lista_ordenada:
        print("\nNo tienes tareas en esta vista.")
        return None
    
    print(f"\n{'N':<3} | {'Fecha Venc.':<12} | {'Estado':<10} | {'Titulo':<25} ")
    print("-" * 63)

    for i, tarea in enumerate(lista_ordenada):
        estado = "Completada" if tarea['Completada'] else "Pendiente"
        fecha_str = tarea['fecha_venc'].strftime('%Y-%m-%d')
        print(f"{i+1:<3} | {fecha_str:<12} | {estado:<10} | {tarea['titulo']:<25}")

    print("-" * 63)
    return lista_ordenada

def MarcarCompletado(username):
    lista_pendientes =_mostrar_y_obtener_lista(username, filtro='pendientes')

    if lista_pendientes is None:
        input ("\nNo hay tareas pendientes. Presione ENTER para volver...")
        return
    
    try:
        print("\nIngrese el N° de la tarea a marcar como completada.")
        num= int(input("N°: "))

        if num < 1 or num > len(lista_pendientes):
            raise IndexError("Número fuera de rango")
        
    except (ValueError, IndexError):
        clearConsole()
        while True:
            print("Entrada inválida. Ingrese número de la lista.")
            op = input("Volver a intentar [1]\nRegresar [2]\nIngrese una opción: ")
            clearConsole()
            match op:
                case "1":
                    MarcarCompletado(username)
                    return
                case "2":
                    return
                case _:
                    print("Opción no valida")

    tarea_a_marcar = lista_pendientes[num-1]
    tarea_a_marcar['completada'] = True

    optionsShow("¡Tarea marcada como completada!", "Volver")
    input("Escoja una opción: ")

def EliminarTarea(username):
        lista_todas = _mostrar_y_obtener_lista(username, filtro='todas')
        
        if lista_todas is None:
            input("\nNo hay tareas para eliminar. Presione ENTER para volver...")
            return
    
        try:
            print("\nIngrese el N° de la tarea que desea ELIMINAR.")
            num = int(input("N°: "))
            
            if num < 1 or num > len(lista_todas):
                raise IndexError("Número fuera de rango")
            
        except (ValueError, IndexError):
            clearConsole()
            while True:
                print("Entrada inválida. Ingrese un número de la lista.")
                op = input("Volver a intentar [1]\nRegresar [2]\nIngrese una opcion: ")
                
                clearConsole()
                match op:
                    case "1":
                        EliminarTarea(username) 
                        return
                    case "2":
                        return
                    case _:
                        print("Opcion no valida")
        tarea_a_eliminar = lista_todas[num-1]
        tareas.remove(tarea_a_eliminar)
        
        optionsShow("¡Tarea eliminada permanentemente!", "Volver")
        input("Escoja una opcion: ")

def MenuTareas(user):
    username = user['username'] 
    
    while True:
        optionsShow(f"--- Gestor de Tareas de {user['username'].split()[0]} ---",
                    "Crear Tarea",
                    "Ver Tareas Pendientes (por fecha)",
                    "Marcar Tarea como Completada",
                    "Ver Tareas Completadas (Historial)",
                    "Eliminar Tarea",
                    "Volver al Menú Principal")
        
        opcion = input("Escoja una opcion: ")
        
        match opcion:
            case "1":
                CrearTarea(username)
            case "2":
                _mostrar_y_obtener_lista(username, filtro='pendientes')
                input("\nPresione ENTER para volver...")
            case "3":
                MarcarCompletado(username)
            case "4":
                _mostrar_y_obtener_lista(username, filtro='completadas')
                input("\nPresione ENTER para volver...")
            case "5":
                EliminarTarea(username)
            case "6":
                break 
            case _:
                clearConsole()
                input("Opción no válida. Presione ENTER para reintentar.")

























    