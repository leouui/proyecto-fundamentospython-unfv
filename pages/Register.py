from helpers import optionsShow, continueUntilCorrect,dynamicInputs
from pages.validations.Register import userCodeValidation,userNameValidation,passwordValidation

def RegisterUser():
    results = dynamicInputs("---------Registro---------",
        ["Ingrese su nombre completo: ",userNameValidation], #results[0]
        ["Ingrese el codigo del estudiante: ",userCodeValidation], #results[1]
        ["Ingrese la contraseña: ",passwordValidation], #results[2]
    )

    if results is None: return

    optionsShow("---Registro satisfactorio!!",
                "Volver")
    
    input("Ingrese una opcion: ")

    return {
        "username":results[0],
        "usercode":results[1],
        "password":results[2],
        "notes":[],
        "courses":{},
        "tasks": [],
        "expenses": []
    }