import random
def desordenar (lista, tamanio_lista, cont):
    if cont<tamanio_lista:
        random.shuffle(lista)
        desordenar(lista, tamanio_lista, cont+1)
    
N = [1,2,3,4,5,6,7,8,9,10]
desordenar(N,len(N),8)
print(N)
