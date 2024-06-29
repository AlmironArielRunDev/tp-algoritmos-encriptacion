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

from funciones.funciones import invertir_letra_cada_palabra

texto_original = input('Ingrese un texto: ')
clave = int(input('Ingrese su clave de seis digitos: '))

resultado = invertir_letra_cada_palabra(texto_original)

print(resultado)
