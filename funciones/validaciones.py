# Funcion para validar que la clave es de tipo entero
def validar_clave(clave):
    while True:
        if clave.isdigit() and len(clave) == 6:
            break
        else:
            print("\n\tERROR. La clave debe ser un número entero de exactamente 6 dígitos.")
            clave = input("\n\tIngrese nuevamente una clave válida: ")
    return int(clave)

