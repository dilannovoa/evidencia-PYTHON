numero = int(input("Ingrese un número: "))

while numero >= 0:
    cuadrado = numero ** 2
    print("El cuadrado de", numero, "es", cuadrado)
    numero = int(input("Ingrese otro número: "))


######################################################

numero = int(input("Ingrese un número entero positivo: "))

while numero != 1:
    if numero % 2 == 0:  # Par
        numero = numero // 2
    else:  # Impar
        numero = 3 * numero + 1

    print(numero, end=" ")

#####################################

poblacion_A = 25
poblacion_B = 18.9
tasa_crecimiento_A = 0.02
tasa_crecimiento_B = 0.03
anio = 2022

while poblacion_B <= poblacion_A:
    poblacion_A += poblacion_A * tasa_crecimiento_A
    poblacion_B += poblacion_B * tasa_crecimiento_B
    anio += 1

print("La población del país B superará a la del país A en el año", anio)



#cada parte del codigo que esta dividido en un punto del problema

