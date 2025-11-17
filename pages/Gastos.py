from helpers import clearConsole, optionsShow, SearchUserByAtr
import datetime 
from database.users import users
from database.actions import modifyDataUser

def _mostrar_gastos(lista_gastos, filtro_categoria=None):
    clearConsole()
    total = 0.0
    
    if filtro_categoria:
        print(f"--- Gastos de '{filtro_categoria}' ---")
        gastos_filtrados = [g for g in lista_gastos if g['categoria'].lower() == filtro_categoria.lower()]
    else:
        print(f"--- Todos los Gastos ---")
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


def RegistrarGasto(user, lista_gastos):
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
    
    nuevo_gasto = {
        "monto": monto,
        "descripcion": descripcion,
        "categoria": categoria,
        "fecha": datetime.date.today() 
    }
    
    # 1. Añadir a la lista local
    lista_gastos.append(nuevo_gasto)

    # 2. Guardar en la base de datos global
    modifyDataUser(user["usercode"], {**user, "expenses": lista_gastos})

    optionsShow("¡Gasto registrado con éxito!", "Agregar otro gasto", "Volver al Menú")
    op = input("Escoja una opcion: ")
    match op:
        case "1":
            RegistrarGasto(user, lista_gastos) 
        case "2":
            return
        case _:
            return

def VerGastosPorCategoria(lista_gastos):
    """Permite al usuario elegir una categoría y filtra los gastos."""
    clearConsole()
    
    if not lista_gastos:
        input("No tienes gastos para filtrar.\nRegresar[ENTER]")
        return

    # Obtenemos las categorías únicas de la lista real
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
                    VerGastosPorCategoria(lista_gastos) 
                    return
                case "2":
                    return 
                case _:
                    print("Opcion no valida")
    
    categoria_seleccionada = categorias[num-1]
    _mostrar_gastos(lista_gastos, filtro_categoria=categoria_seleccionada)

# --- Menú Principal del Módulo ---

def MenuGastos(user):
    
    while True:
        optionsShow(f"--- Control de Gastos de {user['username'].split()[0]} ---",
                    "Registrar Gasto",
                    "Ver Todos los Gastos",
                    "Filtrar Gastos por Categoría",
                    "Volver al Menú Principal")
        
        opcion = input("Escoja una opcion: ")
        clearConsole()

        gastos_actuales = SearchUserByAtr("usercode", user["usercode"], users)[1]["expenses"]
        
        match opcion:
            case "1":
                RegistrarGasto(user, gastos_actuales)
            case "2":
                _mostrar_gastos(gastos_actuales)
            case "3":
                VerGastosPorCategoria(gastos_actuales)
            case "4":
                break
            case _:
                input("Opción no válida. Presione ENTER para reintentar.")