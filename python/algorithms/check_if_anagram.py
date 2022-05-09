#Given two strings, write an algorithm to check if they are anagrams of each other. Return true if they pass the test and false if they don't.

def is_anagram(word1,word2):
    if( len(word2) != len(word1) ):
        return False
    for letter in word1:
        if letter not in word2:
            return False
    return True

print(is_anagram('sileent', 'liisten'))