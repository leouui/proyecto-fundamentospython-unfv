from helpers import optionsShow, continueUntilCorrect
from pages.validations.Register import userCodeValidation,userNameValidation,passwordValidation

def RegisterUser():
    print("---------Registro---------")
    
    userName = continueUntilCorrect("Ingrese su nombre completo: ",userNameValidation)
    if(userName is None): return

    userCode= continueUntilCorrect("Ingrese el codigo del estudiante: ", userCodeValidation)
    if(userCode is None): return

    password = continueUntilCorrect("Ingrese la contraseña: ",passwordValidation)
    if(password is None): return

    optionsShow("---Registro satisfactorio!!","Volver")
    input("Escoja una opcion: ")

    #se puede crear una clase estudiante aqui
    return {
        "username":userName,
        "code":userCode,
        "password":password
    }