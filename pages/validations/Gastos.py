def expenseValidation(expense):
    try:
        expense = float(expense)
        if expense <= 0: return (False,"El monto debe ser positivo.")
    except:
        return (False, "Valor no válido. Debe ser un número positivo (ej. 15.50)")
    
    return (True,expense)

def expenseInfoValidation(str):
    if(len(str.strip()) == 0): return (False,"La cadena no puede ser vacia")
    return (True,str.strip())

def selectCatValidation(cat,categorias):
    try:
        cat=int(cat)
        if cat < 1 or cat > len(categorias): return (False,"Fuera de rango")
    except:
        return (False,"Ingrese una entrada numerica")
    
    return (True,cat)
