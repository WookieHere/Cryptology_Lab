ascii_map = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]


def index_of_letter(input_letter):
    return ascii_map.index(input_letter)

def shift_letter(input_letter, key_letter):
    return ascii_map[(index_of_letter(input_letter) + index_of_letter(key_letter)) % len(ascii_map)]

def encrypt_phrase(input_phrase, input_key):
    new_word = ""
    for i in range(0, len(input_phrase)):
        if input_phrase[i] != ' ':
            new_word += shift_letter(input_phrase[i], input_key[i % len(input_key)])
    print(new_word)

input_phrase = "happy to meet you"
input_key = "no"
encrypt_phrase(input_phrase, input_key)