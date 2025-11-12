import os
import platform

def SearchUserByName(name,users):
    for user in users:
        if(user["name"] == name):
            return (True, user)
    return (False,None)

def clearConsole():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def optionsShow(init,*options):
    clearConsole()
    print(init)
    for (index,msg) in enumerate(options):
        print(f"{msg} [{index + 1}]")