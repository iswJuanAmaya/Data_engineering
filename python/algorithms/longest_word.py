
def get_the_longest_word_of(phrase):
    splited_phrase = phrase.split(" ")
    longest_word = ""
    for word in splited_phrase:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(get_the_longest_word_of('Top Shelf Web Development Training98765 on Scotch')) 