from helpers import continueUntilCorrect
from pages.validations.Login import userCodeValidation,userPasswordValidation

def Login():
    print("---------Inicio de sesion---------")

    user = continueUntilCorrect("Ingrese el codigo del estudiante: ",userCodeValidation)
    if(user is None): return

    password = continueUntilCorrect("Ingrese la contrasenia: ",userPasswordValidation,user)
    if(password is None): return

    return user