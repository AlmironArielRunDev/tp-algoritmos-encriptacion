import re
from tda.tda_pilas import Pila, apilar, desapilar, pila_vacia

# Primer paso: Función para invertir los caracteres de cada palabra
def invertir_letra_cada_palabra(texto_original):
    palabras = texto_original.split(' ')
    caracteres_invertidos = []

    for palabra in palabras:
        pila = Pila()
        for caracter in palabra:
            apilar(pila, caracter)
        
        caracter_invertido = ''
        while not pila_vacia(pila):
            caracter_invertido += desapilar(pila)
        
        caracteres_invertidos.append(caracter_invertido)

    return ' '.join(caracteres_invertidos)

# Segundo paso: Función para invertir el orden de las palabras
def invertir_orden_palabras(texto_original):
    palabras = texto_original.split(' ')
    pila = Pila()
    
    for palabra in palabras:
        apilar(pila, palabra)
    
    palabras_invertidas = ''
    while not pila_vacia(pila):
        palabras_invertidas += desapilar(pila) + ' '
    
    return palabras_invertidas.strip()

def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ''
    for caracter in texto:
        if 32 <= ord(caracter) <= 126:  # Considerar solo caracteres imprimibles
            nuevo_orden = (ord(caracter) - 32 + desplazamiento) % (126 - 32 + 1) + 32
            texto_cifrado += chr(nuevo_orden)
        else:
            texto_cifrado += caracter  # Dejar los caracteres no imprimibles sin cambios
    return texto_cifrado



# Cuarto paso: Función para invertir el texto completamente
def invertir_texto_completo(texto):
    pila = Pila()
    for caracter in texto:
        apilar(pila, caracter)
    texto_invertido = ''
    while not pila_vacia(pila):
        texto_invertido += desapilar(pila)
    return texto_invertido
