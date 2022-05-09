#Given a string of text containing 0 or more vowels, count the number of vowels that can be found within the text. 

def count_vowels(word):
    vowels = ["A","E","I","O","U","a","e","i","o","u"]
    counter = 0
    for letter in word:
        if letter in vowels:
            counter += 1
    return counter

print(count_vowels("juan grcia"))

