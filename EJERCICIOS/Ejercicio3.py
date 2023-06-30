

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)


n = int(input("Ingrese un número natural: "))

print("Números y sus factoriales:")
for numero in range(1, n + 1):
    fact = factorial(numero)
    print(numero, fact)
