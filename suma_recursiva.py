def suma (x,y):
    if y ==0:
        return x
    else:
        return suma (x,y-1)+1
        
print(suma(2,100))