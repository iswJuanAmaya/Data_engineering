#Given a string of text, write an algorithm that returns the text received in a reversed format. 

def reverse(word):
    try:
        reversed_word = ''
        for letter in reversed(word):
            reversed_word += letter
        return reversed_word
    except Exception as error:
        return(f"error: {error}")

print(reverse("123456789"))