from helpers import SearchUserByAtr
from database.users import users

def userCodeValidation(userCode):
    (find,user) = SearchUserByAtr("code",userCode,users)

    if(not(find)): return (False, "No se encontro el estudiante")

    return (True,user)
            
def userPasswordValidation(password,user):
    if(user["password"] != password): return (False,"Contrasenia incorrecta")

    return (True,password)
