from tda.tda_colas import Cola, agregar, sacar, cola_vacia
from tda.tda_pilas import Pila, apilar, desapilar, pila_vacia

 # Funciones para el cifrado y descifrado
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

def invertir_texto(texto):
    cola = Cola()
    for caracter in texto:
        agregar(cola, caracter)
    
    texto_invertido = ""
    while not cola_vacia(cola):
        texto_invertido = sacar(cola) + texto_invertido
    
    return texto_invertido