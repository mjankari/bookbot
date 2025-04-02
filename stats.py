def get_num_words(words_list:list[str]):
    '''
    Print number of words found in a document.
    '''
    print(f"Found {len(words_list)} total words")

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

def sort_list(input:list):
    '''
    Takes the dictionary of characters and their counts and returns a sorted
    list of dictionaries
    '''
    input_list = []

    # Convert each key-value pair to a dictionary
    for char, count in input.items():
        input_list.append({"char": char, "count": count})

    # Define a helper function for sorting
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list in descending order
    input_list.sort(reverse=True, key=sort_on)

    return input_list
