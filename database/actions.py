import json
from database.users import users
from helpers import SearchUserByAtr
from ruta import ruta

def addUser(user):
    users.append(user)

    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(json.dumps(users))

def modifyDataUser(usercode,newData):
    searchResults = SearchUserByAtr("usercode",usercode,users)
    if(searchResults[0]):
        users[searchResults[2]] = newData
        
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(json.dumps(users))