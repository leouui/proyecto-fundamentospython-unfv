def noteTitlevalidation(note):
    if(len(note.strip()) == 0):
        return (False,"Ingrese una nota valida")
    
    return (True,note)

def numNotesvalidation(nota,notas):
    try:
        num = int(nota)
        if(num>len(notas) or num<0): return (False,"No existe esa nota")
    except:
        return (False,"La entrada no es numerica")

    return (True,int(nota))