#Given two strings of equal length, calculate and return the the hamming distance

def get_hamming_distance(word1,word2):
    counter = 0
    if( len(word1) == len(word2) ):
        for letter1,letter2 in zip(word1,word2):
            if(letter1 != letter2):
                counter += 1
    else:
        min_lenght = min(len(word1),len(word2))
        for i in range(min_lenght):
            if word1[i] != word2[i]:
                counter += 1
        counter += abs(len(word1)-len(word2))
    return counter              

print(get_hamming_distance("pazart","pisarrr"))
