#Given a string of text, return true or false indicating whether or not the text is a palindrome.

def check_if_palindrome(word):
    reversed_word = ''
    for letter in reversed(word):
        reversed_word += letter
    if word == reversed_word:
        return True
    else:
        return False

print(check_if_palindrome("racecarr"))
