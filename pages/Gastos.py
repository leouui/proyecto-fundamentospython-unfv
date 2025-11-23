import datetime 
from helpers import clearConsole, optionsShow, SearchUserByAtr, dynamicInputs
from .validations.Gastos import expenseValidation,expenseInfoValidation,selectCatValidation
from database.actions import modifyDataUser
from database.users import users

def MostrarGastos(lista_gastos, filtro_categoria=None):
    total = 0.0
    
    if filtro_categoria:
        print(f"--- Gastos de '{filtro_categoria}' ---")
        gastos_filtrados = []

        for gasto in lista_gastos:
             if gasto['categoria'].lower() == filtro_categoria.lower():
                gastos_filtrados.append(gasto)
    else:
        print(f"--- Todos los Gastos ---")
        gastos_filtrados = lista_gastos

    if not gastos_filtrados:
        return input("--> No hay gastos en esta vista.\nRegresar[ENTER] ")

    print(f"\n{'Fecha':<12} | {'Monto (S/)':<12} | {'Categoría':<15} | {'Descripción':<20}")

    print("-" * 64)
    for gasto in gastos_filtrados:
        fecha_str = gasto['fecha'].strftime('%Y-%m-%d')
        monto_str = f"S/ {gasto['monto']:.2f}" 
        total += gasto['monto']
        print(f"{fecha_str:<12} | {monto_str:<12} | {gasto['categoria']:<15} | {gasto['descripcion']:<20}")
    print("-" * 64)

    print(f"TOTAL GASTADO (en esta vista): S/ {total:.2f}")
    input("Regresar[ENTER] ")

def RegistrarGasto(user, expenses):
    results = dynamicInputs("--- Registrar Nuevo Gasto ---",
        ["Monto del gasto (ej. 15.50): ", expenseValidation], #results[0]
        ["Descripción (ej. 'Almuerzo'): ",expenseInfoValidation], #results[1]
        ["Categoría (ej. 'Comida', 'Transporte'): ",expenseInfoValidation] #results[2]
    )

    nuevo_gasto = {"monto": results[0],"descripcion": results[1],"categoria": results[2].capitalize(),"fecha": datetime.date.today() }
    
    expenses.append(nuevo_gasto)
    modifyDataUser(user["usercode"], {**user, "expenses": expenses})

    input("--> ¡Gasto registrado con éxito!.\nRegresar[ENTER]")
 
def VerGastosPorCategoria(lista_gastos):    
    if not lista_gastos:
        return input("No tienes gastos para filtrar.\nRegresar[ENTER]")

    categorias = sorted(list(set(g['categoria'] for g in lista_gastos)))

    l = "Filtrar Gastos por Categoría - Elige una:"
    for i, cat in enumerate(categorias):
        l+=f"\n[{i+1}] {cat}"
    l += f"\n{'-' * 30}"

    results = dynamicInputs(l,
        ["Ingrese el N° de categoría: ",selectCatValidation,categorias] # results[0]
    )
    if results is None: return

    clearConsole()
    categoria_seleccionada = categorias[results[0]-1]
    MostrarGastos(lista_gastos, filtro_categoria=categoria_seleccionada)

def MenuGastos(user):
    while True:
        optionsShow(f"--- Control de Gastos de {user['username'].split()[0]} ---",
                    "Registrar Gasto",
                    "Ver Todos los Gastos",
                    "Filtrar Gastos por Categoría",
                    "Salir")
        
        opcion = input("Ingrese una opcion: ")
        clearConsole()

        expenses = SearchUserByAtr("usercode", user["usercode"], users)[1]["expenses"]
        
        match opcion:
            case "1": RegistrarGasto(user, expenses)
            case "2": MostrarGastos(expenses)
            case "3": VerGastosPorCategoria(expenses)
            case "4": break
            case _: input("--> Ingrese una opcion valida\nContinuar[ENTER] ")