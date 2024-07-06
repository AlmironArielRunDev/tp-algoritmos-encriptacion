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

import os
import time
from funciones.funciones import invertir_letra_cada_palabra, invertir_orden_palabras, invertir_texto_completo, cifrado_cesar
from funciones.validaciones import validar_clave

# Función para encriptar el texto
# -------------------------------
def encriptar(texto_original, clave):
    desplazamiento = clave % 26
    if desplazamiento == 0:
        desplazamiento = 3

    # 1. Invierte cada palabra del texto
    resultado_invertir_letras = invertir_letra_cada_palabra(texto_original)
    
    # 2. Invierte el orden de las palabras del texto
    resultado_invertir_orden = invertir_orden_palabras(resultado_invertir_letras)
    
    # 3. Aplica el cifrado César al texto completo
    resultado_cifrado = cifrado_cesar(resultado_invertir_orden, desplazamiento)
    
    # 4. Invierte el texto completo
    resultado_final = invertir_texto_completo(resultado_cifrado)
    
    return resultado_final


# Función para descifrar el texto
def descifrar(texto_cifrado, clave):
    desplazamiento = clave % 26
    if desplazamiento == 0:
        desplazamiento = 3
    desplazamiento = -desplazamiento  # Desplazamiento negatívo para descifrar

    # 1. Invierte el texto completamente
    resultado_invertido = invertir_texto_completo(texto_cifrado)
    
    # 2. Aplica el descifrado César al texto completo
    resultado_descifrado = cifrado_cesar(resultado_invertido, desplazamiento)
    
    # 3. Invierte el orden de las palabras del texto
    resultado_ordenado = invertir_orden_palabras(resultado_descifrado)
    
    # 4. Invierte cada palabra del texto
    resultado_final = invertir_letra_cada_palabra(resultado_ordenado)
    
    return resultado_final




# Pedir el texto original y la clave del usuario
texto_original = input('Ingrese un texto: ')

clave = input('Ingrese su clave de seis dígitos: ')
clave = validar_clave(clave)

os.system('cls')
print('Encriptando texto...')
time.sleep(1)
os.system('cls')


# Encriptar el texto
texto_encriptado = encriptar(texto_original, clave)
print(f'Texto encriptado: {texto_encriptado}')
print('')

# Desencriptar el texto
texto_desencriptado = descifrar(texto_encriptado, clave)
print(f'Texto desencriptado: {texto_desencriptado}')
print('')

# texto original: ariel almiron
# invertir caracteres: norimla leira
# cifrado César: opsjnmb!mfjsb

# Resultado Final: bsjfm!bmnjspo
