#Given a string of text, find and return the most recurring character

def get_the_most_recurring_value(string):
    lista_de_caracteres = {}
    for letter in string:
        x = lista_de_caracteres.get(letter)
        if x is None:
            lista_de_caracteres[letter] = 1
        else:
            lista_de_caracteres[letter] = (x+1)
    #values = lista_de_caracteres.values()
    #return max(values)
    return max(lista_de_caracteres, key=lista_de_caracteres.get)


print(get_the_most_recurring_value('bbaauj'))