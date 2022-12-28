import time 
def fibo_recursivo(num):
    if num ==0 or num ==1:
        return 1
    else:
        return fibo_recursivo(num-1) + fibo_recursivo(num-2)

tiempo = time.perf_counter() 
fibo_recursivo(10)
tiempo1 = time.perf_counter() 
print("Tiempo del Fibonacci recursivo: ", tiempo1-tiempo)


def fibo_normal(n):
    x = 0
    y = 1

    for i in range (n+1):
        z = x + y
        x = y
        y = z
    return x
tiempo = time.perf_counter() 
fibo_normal(10)
tiempo1 = time.perf_counter() 
print("Tiempo del Fibonacci no recursivo: ", tiempo1-tiempo)