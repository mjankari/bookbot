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

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    book_word_number = len(split_book_content(book_text))
    print(f"{book_word_number} words found in the document")

main()
