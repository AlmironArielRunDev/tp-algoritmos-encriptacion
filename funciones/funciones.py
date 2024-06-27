from tda.tda_colas import Cola, agregar, sacar, cola_vacia
from tda.tda_pilas import Pila, apilar, desapilar, pila_vacia

 # Funciones auxiliares para el cifrado y descifrado
def invertir_palabra(palabra):
    pila = Pila()
    for caracter in palabra:
        apilar(pila, caracter)
    
    palabra_invertida = ""
    while not pila_vacia(pila):
        palabra_invertida += desapilar(pila)
    
    return palabra_invertida

def invertir_orden_palabras(texto):
    palabras = texto.split()
    pila = Pila()
    
    for palabra in palabras:
        apilar(pila, palabra)
    
    texto_invertido = ""
    while not pila_vacia(pila):
        texto_invertido += desapilar(pila) + " "
    
    return texto_invertido.strip()

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_offset = 65 if caracter.isupper() else 97
            resultado += chr((ord(caracter) - ascii_offset + desplazamiento) % 26 + ascii_offset)
        else:
            resultado += caracter
    return resultado

def invertir_texto(texto):
    cola = Cola()
    for caracter in texto:
        agregar(cola, caracter)
    
    texto_invertido = ""
    while not cola_vacia(cola):
        texto_invertido = sacar(cola) + texto_invertido
    
    return texto_invertido

def encriptar(texto, clave):
    # Paso 1: Invertir cada palabra del texto
    palabras_invertidas = " ".join(invertir_palabra(palabra) for palabra in texto.split())
    
    # Paso 2: Invertir el orden de las palabras del texto
    texto_invertido_orden_palabras = invertir_orden_palabras(palabras_invertidas)
    
    # Paso 3: Aplicar el método del César
    desplazamiento = sum(int(digito) for digito in str(clave)) % 26
    if desplazamiento == 0:
        desplazamiento = 3
    texto_cifrado = cifrado_cesar(texto_invertido_orden_palabras, desplazamiento)
    
    # Paso 4: Invertir el texto completo
    texto_final = invertir_texto(texto_cifrado)
    
    return texto_final

def desencriptar(texto, clave):
    # Paso 4: Invertir el texto completo
    texto_invertido = invertir_texto(texto)
    
    # Paso 3: Aplicar el método del César con desplazamiento negativo
    desplazamiento = sum(int(digito) for digito in str(clave)) % 26
    if desplazamiento == 0:
        desplazamiento = 3
    texto_descifrado = cifrado_cesar(texto_invertido, -desplazamiento)
    
    # Paso 2: Invertir el orden de las palabras del texto
    texto_orden_invertido = invertir_orden_palabras(texto_descifrado)
    
    # Paso 1: Invertir cada palabra del texto
    palabras_originales = " ".join(invertir_palabra(palabra) for palabra in texto_orden_invertido.split())
    
    return palabras_originales