def calcular_epsilon_maquina():
    epsilon = 1.0

    while 1.0 + epsilon != 1.0:
        epsilon /= 2.0

    return epsilon


epsilon_maquina = calcular_epsilon_maquina()
print("El épsilon de la máquina es:", epsilon_maquina)



####################
#este es el codigo de un ejercicio