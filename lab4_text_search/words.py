def get_words(input_text):
    words = []
    curr_word = ""
    for char in input_text:
        if char != ' ' and char != '\n' and char != ',':
            curr_word += char
        else:
            words.append(curr_word)
            curr_word = ""

    return words
