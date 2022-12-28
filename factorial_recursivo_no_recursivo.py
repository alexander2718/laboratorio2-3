import time
def factorial_recursivo(n):
    if n==1:
        return 1 
    return n*factorial_recursivo(n-1)

tiempo_requerido = time.perf_counter()
X = factorial_recursivo(5)

tiempo_requerido1 = time.perf_counter()

print("El factorial recursivo de: ", X, "se hizo en: ", tiempo_requerido1-tiempo_requerido)

def factorial_no_recursivo(n):
    a = 1
    for i in range (n,1,-1):
        a=a*i
    return a
tiempo_requerido = time.perf_counter()
Y = factorial_no_recursivo(5)
tiempo_requerido1 = time.perf_counter()
print("El factorial no recursivo de: ", Y, "se hizo en: ", tiempo_requerido1-tiempo_requerido)





