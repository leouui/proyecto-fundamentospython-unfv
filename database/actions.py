from database.users import users
from helpers import SearchUserByAtr

def addUser(user):
    users.append(user)

def modifyDataUser(usercode,newData):
    searchResults = SearchUserByAtr("usercode",usercode,users)
    if(searchResults[0]):
        users[searchResults[2]] = newData