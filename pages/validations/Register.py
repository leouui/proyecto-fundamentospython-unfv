from helpers import SearchUserByAtr
from database.users import users

def userNameValidation(userName):
    if(len(userName.strip()) == 0): return (False,"El nombre es incorrecto")

    return (True,userName)

def userCodeValidation(code):
    if(len(code)!=10): return (False, "El codigo debe tener 10 digitos")
    
    if(SearchUserByAtr("usercode",code,users)[0]): return (False,"El codigo de estudiante ya existe")

    return (True,code)

def passwordValidation(password):
    if(len(password)<6): return (False, "La contraseña debe tener al menos 7 caracteres")

    return (True,password)
