#Given a sentence containing two or more words, return the equivalent of the sentence when capitalized

def capitalization_of_sentence(sentence):
    splited_sentence = sentence.split(" ")
    new_sentence = ""
    for word in splited_sentence:
        upperCase = word[0].upper()
        new_sentence += upperCase + word[1:]+" "
    return new_sentence

print(capitalization_of_sentence("the tales of scotch!"))