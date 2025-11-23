def courseTitlevalidation(title,materias):
    title = title.upper()

    if(len(title.strip()) == 0): return (False,"Ingrese un nombre valido")
    if title in materias: return (False,"La materia ya existe")
   
    return (True,title)
def selectCoursevalidation(num,materias):
    try:
        num = int(num)
        if num>(len(materias)) or num<0: return(False,"Materia no encontrada")
    except:
        return (False,"Valor no numerico")
    
    return (True,num)
def floatValidation(num):
    try:
        num=float(num)
    except:
        return (False,"Ingrese una valor numerico")
    
    return (True,num)