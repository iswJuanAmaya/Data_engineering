from typing import Tuple, Dict, List
#mypy
#---------------------------------------

a: int = 5
print(a)


b: str = 'hola mundo'
print(b)
#---------------------------------------

def  suma(a: int, b: int) -> int:
    return a + b

print(suma(1,2))
#-------------------------------------------------

CoordinatesType = List[Dict[str, Tuple[int,int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1,2),
        'coord2': (3,4)
    },
    {
        'coord1': (5,6),
        'coord2': (7,8)
    },
]