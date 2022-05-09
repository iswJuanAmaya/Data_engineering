"""Decorador: Es una funcion que recibe como parametro otra funcion, le añade cosas y retorna una funcion diferente.
   Una funcion que le añade super poderes a otra funcion."""

def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura

def saludo():
    print("¡Hola!")

saludo()
# ¡Hola!

saludo = decorador(saludo) # Se guarda la función decorada en la variable saludo
saludo()   
# Esto se añade a mi función original.
# ¡Hola!
#------------------------------------------------------------------------------------------------------------------------------------------
# De esta manera se decora la función saludo (equivale a saludo = decorador(saludo) de la última línea, quedando ahora en la línea inmediata superior ):
@decorador                
def saludo():
    print("¡Hola!")

saludo()                   # La función saludo está ahora decorada 
# Esto se añade a mi función original.
# ¡Hola!

#-------------------------------------------------------------------------------
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibistes un mensaje'

print(mensaje('duvan'))