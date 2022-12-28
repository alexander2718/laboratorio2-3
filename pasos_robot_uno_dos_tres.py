def pasos_robot(n):
    if n == 1 or n ==2:
        return n
    elif n == 3:
        return n+1
    return pasos_robot(n-1) + pasos_robot(n-2)

print(pasos_robot(8))