def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n = int(input("ingresa un numero para conocer la secuencia "))
print("serie de fibonacci")
for n in range(0,n):
    print(fibonacci(n))