def potencia (x,y):
    if y ==1:
        return x
    else:
        return potencia (x,y-1)*x

print(potencia(8,2))