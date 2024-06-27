class nodoPila(object):
    info, sig = None, None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0
        
def apilar(pila, dato):
    """Apila el dato sobre la cima de la pila"""
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1
    
def desapilar(pila):
    """Desapila el elemento en la cima de la pila y lo devuelve"""
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio += 1
    return x
    
def pila_vacia(pila):
    """Devuelve True si la pila está vacía"""
    return pila.cima is None
    
def en_cima(pila):
    """Devuelve el valor almacenado en la cima de la pila"""    
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None
    
def tamanio_pila(pila):
    """Devuelve el numero de elementos en la pila"""
    return pila.tamanio

def mostrar_pila(pila):
    paux = Pila()
    while(not pila_vacia(pila)):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
        
    while(not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(pila, dato)
        
    