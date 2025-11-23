import datetime #libreria para manejar fechas y horas

def tareaTitlevalidation(title):
    if not title: return (False, "El titulo no puede estar vacío")
    return (True,title)

def tareaFechaValidation(date):
    try:
        fecha_valida = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        if fecha_valida < datetime.date.today(): 
            return (False,f"Advertencia: La fecha '{date}' ya pasó.")
    except:
        return (False,"Fecha incorrecta")

    return (True,date)

def numTareaValidation(num,tareas):
    try:
        num = int(num)
        if num < 1 or num > len(tareas): return (False,"La tarea no existe")
    except:
        return (False,"La entrada debe ser numerica")
    
    return (True,num)