"""Realizar un programa que permita encriptar y desencrpitar un texto ingresado por el usuario. 
Además el usuario ingresa una clave numérica asociada de 6 dígitos. 
El método de encriptación se hará de la siguiente manera:
1) Invertir cada palabra del texto
2) Invertir el orden de las palabras del texto
3) Aplicar al texto completo el método del César. 
La clave numérica sirve para calcular el desplazamiento de cada caracter del texto. 
Nota: tener en cuenta la cantidad de caracteres del alfabeto y en el caso de dar cero sumar 3
4) Invertir el texto completo

Nota final ejercicio: aplicar la TAD de pilas y se puede usar la del trabajo anterior"""

# from funciones.funciones import encriptar, desencriptar 

# Ejemplo de uso
texto_original = input('Ingrese un texto: ')
clave = int(input('Ingrese su clave de seis digitos: '))

# texto_encriptado = encriptar(texto_original, clave)
# print(f"Texto encriptado: {texto_encriptado}")

# texto_desencriptado = desencriptar(texto_encriptado, clave)
# print(f"Texto desencriptado: {texto_desencriptado}")
