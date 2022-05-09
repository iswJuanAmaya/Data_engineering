from time import sleep

#---------- Asi funciona un ciclo for realmente.------------------ #
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

# Iterando un iterador
while True: #ciclo infinito
  try:
    element = next(my_iter)
    #print(element)
  except StopIteration:
    break

#---------- Forma base de un iterador en clase------------------#
class EvenNumber:
    """Clase que implementa un iterador de todos los números pares, o los números pares hasta un máximo."""
    def __init__(self,max=None):
        self.max = max


    def __iter__(self):
        self.num = 0
        return self


    def __next__(self):
        if not self.max or self.num <= self.max:
            result= self.num
            self.num += 2
            return result
        else:
            raise StopIteration
 

 #---------------------
class FiboIter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

if __name__ == '__main__':
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        sleep(1)