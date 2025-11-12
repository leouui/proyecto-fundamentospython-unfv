from helpers import optionsShow,clearConsole
def App(data):    
    while True:
        optionsShow(f"---------Bienvenido {data['username'].split()[0]} 🖐🖐---------",
                    "Gestor de Tareas y Recordatorios",
                    "Control de Gastos Estudiantiles",
                    "Organizador de Apuntes",
                    "Calculadora Académica Avanzada",
                    "Salir")

        option = int(input("Escoja una opcion: "))
        clearConsole()
        
        match option:
            case 1:
                print("Gestor de Tareas y Recordatorios")
            case 2:
                print("Control de Gastos Estudiantiles")
            case 3:
                print("Organizador de Apuntes")
            case 4:
                print("Calculadora Académica Avanzada")
            case 5:
                break
            case __:
                print("Ingrese una opcion correcta")