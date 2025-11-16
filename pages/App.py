from helpers import optionsShow,clearConsole
from .Apuntes import MenuApuntes
from .CalcAcademica import MenuCalculadora
from .Tareas import MenuTareas
from .Gastos import MenuGastos

def App(data):    
    while True:
        optionsShow(f"---------Bienvenido {data['username'].split()[0]} 🖐🖐---------",
                    "Gestor de Tareas",
                    "Control de Gastos Estudiantiles",
                    "Organizador de Apuntes",
                    "Calculadora Académica Avanzada",
                    "Salir")

        option = int(input("Escoja una opcion: "))
        clearConsole()
        
        match option:
            case 1:
                MenuTareas(data)
            case 2:
                MenuGastos(data)
            case 3:
                MenuApuntes(data)
            case 4:
                MenuCalculadora(data)
            case 5:
                break
            case __:
                print("Ingrese una opcion correcta")