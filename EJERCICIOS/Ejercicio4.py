def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios

    # Comparar la cadena con su reverso
    if cadena == cadena[::-1]:
        return True
    else:
        return False


cadena = input("Ingrese una cadena de caracteres: ")

if es_palindromo(cadena):
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")




