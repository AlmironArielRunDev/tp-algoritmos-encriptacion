class nodoCola(object):
    """clase nodo cola"""
    info, sig = None, None
    
class Cola(object): 
    def __init__(self):
        """crear cola vacia"""
        self.frente = None
        self.final = None
        self.tamanio = 0
        
def agregar(cola, dato):
    """agrega el dato al final de la cola"""
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1
    
def sacar(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato
    
def cola_vacia(cola):
    return cola.frente is None
    
def en_frente(cola):
    return cola.frente.info

def tamanio(cola):
    return cola.tamanio

def mover_al_final(cola):
    dato = sacar(cola)
    agregar(cola, dato)
    return dato    
    
def mostrar_cola(cola):
    caux = Cola()
    while(not cola_vacia(cola)):
        dato = sacar(cola)
        print(dato)
        agregar(caux, dato)
        
    while(not cola_vacia(caux)):
        dato = sacar(caux)
        agregar(cola, dato)