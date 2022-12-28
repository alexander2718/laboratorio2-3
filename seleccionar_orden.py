def selec_orden (lista, tamanio_lista,cont):
    if cont < tamanio_lista:
        pequenio = lista [cont]
        posicion = cont
        for i in range (cont+1, tamanio_lista):
            if lista[i] < pequenio:
                pequenio = lista[i]
                posicion = i
        lista[cont], lista[posicion] = lista[posicion], lista[cont]
        selec_orden(lista, tamanio_lista,cont+1)

N = [20,19,15,11,12,13,17,18,16]
selec_orden(N, len(N), 0)
print(N)
