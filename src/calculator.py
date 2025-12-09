def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multi(a,b):
    return a*b

def div(a,b):
    if(b == 0):
        return "error"
    return a/b

def power(a,b):
    value = 1
    for x in range(b):
        value = value*a
    
    return value
