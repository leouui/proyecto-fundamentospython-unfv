def courseTitlevalidation(title):
    if(len(title.strip()) == 0):
        return (False,"Ingrese un nombre valido")
   
    return (True,title)