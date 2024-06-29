import re
from tda.tda_pilas import Pila, apilar, desapilar, pila_vacia

def invertir_letra_cada_palabra(texto_original):
    palabras = texto_original.split(' ')
    palabras_invertidas = []

    for palabra in palabras:
        pila = Pila()
        for caracter in palabra:
            apilar(pila, caracter)
        
        palabra_invertida = ''
        while not pila_vacia(pila):
            palabra_invertida += desapilar(pila)
        
        palabras_invertidas.append(palabra_invertida)

    return ' '.join(palabras_invertidas)


# Invierte el orden de las palabras
def invertir_palabra(palabras_invertidas):
    palabra = re.split(r'(\s+)', palabras_invertidas)
    pila = Pila()
    
    for caracter in palabra:
        apilar(pila, caracter)
    
    palabra_invertida = ""
    while not pila_vacia(pila):
        palabra_invertida += desapilar(pila)
    
    return palabra_invertida















# def invertir_orden_palabras(texto):
#     palabras = texto.split()
#     pila = Pila()
    
#     for palabra in palabras:
#         apilar(pila, palabra)
    
#     texto_invertido = ""
#     while not pila_vacia(pila):
#         texto_invertido += desapilar(pila) + " "
    
#     return texto_invertido.strip()

# def invertir_texto(texto):
#     cola = Cola()
#     for caracter in texto:
#         agregar(cola, caracter)
    
#     texto_invertido = ""
#     while not cola_vacia(cola):
#         texto_invertido = sacar(cola) + texto_invertido
    
#     return texto_invertido