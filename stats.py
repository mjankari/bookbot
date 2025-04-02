def get_num_words(words_list:list[str]):
    '''
    Print number of words found in a document.
    '''
    print(f"{len(words_list)} words found in the document")

def count_characters(text:str):
    '''
    Takes the text from the book as a string, and returns the number of times
    each character, (including symbols and spaces), appears in the string
    '''
    characters = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in characters:
            characters[char_lower] += 1
        else:
            characters[char_lower] = 1
    return characters
