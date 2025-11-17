from helpers import clearConsole, optionsShow
import datetime 

gastos_db = {}

def _get_gastos_usuario(username):
    """Obtiene la lista de gastos del usuario actual. La crea si no existe."""
    if username not in gastos_db:
        gastos_db[username] = [] 
    return gastos_db[username]

def _mostrar_gastos(username, filtro_categoria=None):

    clearConsole()
    lista_gastos = _get_gastos_usuario(username)
    total = 0.0
    
    if filtro_categoria:
        print(f"--- Gastos de '{filtro_categoria}' ---")

        gastos_filtrados = [g for g in lista_gastos if g['categoria'].lower() == filtro_categoria.lower()]
    else:
        print(f"--- Todos los Gastos de {username.split()[0]} ---")
        gastos_filtrados = lista_gastos

    if not gastos_filtrados:
        print("\nNo hay gastos en esta vista.")
        input("\nPresione ENTER para volver...")
        return 

    print(f"\n{'Fecha':<12} | {'Monto (S/)':<12} | {'Categoría':<15} | {'Descripción':<20}")
    print("-" * 64)
    for gasto in gastos_filtrados:
        fecha_str = gasto['fecha'].strftime('%Y-%m-%d')
        monto_str = f"S/ {gasto['monto']:.2f}" 
        total += gasto['monto']
        print(f"{fecha_str:<12} | {monto_str:<12} | {gasto['categoria']:<15} | {gasto['descripcion']:<20}")
    
    print("-" * 64)
    print(f"TOTAL GASTADO (en esta vista): S/ {total:.2f}")
    input("\nPresione ENTER para volver...")


def RegistrarGasto(username):
    """Registra un nuevo gasto, con validación de monto."""
    monto = 0.0

    while True:
        clearConsole()
        print("--- Registrar Nuevo Gasto ---")
        try:
            monto_str = input("Monto del gasto (ej. 15.50): ")
            monto = float(monto_str)
            if monto <= 0:
                raise ValueError("El monto debe ser positivo.")
            break 
        except ValueError:
            clearConsole()
            input("Valor no válido. Debe ser un número positivo (ej. 15.50).\nPresione ENTER para reintentar.")

    descripcion = input("Descripción (ej. 'Almuerzo'): ")
    categoria = input("Categoría (ej. 'Comida', 'Transporte'): ").capitalize()
    
    lista_gastos = _get_gastos_usuario(username)
    
    nuevo_gasto = {
        "monto": monto,
        "descripcion": descripcion,
        "categoria": categoria,
        "fecha": datetime.date.today() 
    }
    lista_gastos.append(nuevo_gasto)

    optionsShow("¡Gasto registrado con éxito!", "Agregar otro gasto", "Volver al Menú")
    op = input("Escoja una opcion: ")
    match op:
        case "1":
            RegistrarGasto(username)
        case "2":
            return
        case _:
            return

def VerGastosPorCategoria(username):
    """Permite al usuario elegir una categoría y filtra los gastos."""
    clearConsole()
    lista_gastos = _get_gastos_usuario(username)
    
    if not lista_gastos:
        input("No tienes gastos para filtrar.\nRegresar[ENTER]")
        return

    categorias = sorted(list(set(g['categoria'] for g in lista_gastos)))
    
    print("Filtrar Gastos por Categoría - Elige una:")
    for i, cat in enumerate(categorias):
        print(f"[{i+1}] {cat}")
    print("-" * 30)

    try:
        num = int(input("N° de categoría: "))
        if num < 1 or num > len(categorias):
            raise IndexError("Fuera de rango")
    except (ValueError, IndexError):
        clearConsole()
        while True:
            print("Entrada inválida. Ingrese un número de la lista.")
            op = input("Volver a intentar [1]\nRegresar [2]\nIngrese una opcion: ")
            clearConsole()
            match op:
                case "1":
                    VerGastosPorCategoria(username) 
                    return
                case "2":
                    return 
                case _:
                    print("Opcion no valida")
    
    categoria_seleccionada = categorias[num-1]
    _mostrar_gastos(username, filtro_categoria=categoria_seleccionada)

# --- Menú Principal del Módulo ---

def MenuGastos(user):
    username = user['username']
    
    while True:
        optionsShow(f"--- Control de Gastos de {user['username'].split()[0]} ---",
                    "Registrar Gasto",
                    "Ver Todos los Gastos",
                    "Filtrar Gastos por Categoría",
                    "Volver al Menú Principal")
        
        opcion = input("Escoja una opcion: ")
        clearConsole()
        
        match opcion:
            case "1":
                RegistrarGasto(username)
            case "2":
                _mostrar_gastos(username)
            case "3":
                VerGastosPorCategoria(username)
            case "4":
                break
            case _:
                input("Opción no válida. Presione ENTER para reintentar.")