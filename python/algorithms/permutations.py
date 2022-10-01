import itertools

"""given an array of distinct integers, return all the posible permutations. 
   you can return the answer in any order

En el ejercicio anterior de traté de mostrar algunas de mis buenas practicas, 
mias y algunas otras propias del mismo lenguaje, en este caso he querido demostrar 
que soy además pragmatico, entiendo que a veces lo más importante es el resultado 
y no tanto el tiempo gastando en llegar a ese resultado, las librerías están ahí para usarse,
en este caso python se especializa en ciencia de datos por lo cual tiene un monton de 
herramientas que no facilitan la vida, en este caso itertools que es una librería que conocí 
en uno de mis cursos de python o de ciencia de datos(no recuerdo bien) y permite obtener las 
permutaciones de una lista, he hecho uso de ese modulo y asi mismo me he encargado de las restricciones.
Aveces no tienes que inventar la rueda si la rueda ya existe"
"""

#entry point
if __name__ == "__main__":
    nums = [1,2,3]

    #checa que la cantidad en numeros en la lista este entre 1 y 6
    assert len(nums) in range(1,8)

    #checa que todos los numeros sean distintos/unicos
    assert len(set(nums)) == len(nums)

    #checa si los numeros están en el rango -10 a 10
    for num in nums:
        assert num in range(-10,11)
    print(list(itertools.permutations(nums)))