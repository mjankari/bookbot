import sys
from stats import get_num_words, count_characters, sort_list

def get_book_text(filepath:str):
    '''
    Takes a filepath as input and returns the contents of the file as a string.
    '''
    with open(filepath) as book:
        book_content = book.read()
    return book_content

def split_book_content(text:str):
    '''
    Accepts the text from the book as a string, and returns the number of words
    in the string.
    '''
    words = text.split()
    return words

def check_arguments():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return arguments[1]

def main():
    book_filepath = check_arguments()
    book_text = get_book_text(book_filepath)
    book_split = split_book_content(book_text)
    char_count = count_characters(book_text)
    sorted_list = sort_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}")
    print("----------- Word Count ----------")
    get_num_words(book_split)
    print("--------- Character Count -------")
    for char_dict in sorted_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['count']}")
    print("============= END ===============")

main()
