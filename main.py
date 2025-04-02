def get_book_text(filepath:str):
    '''
    Takes a filepath as input and returns the contents of the file as a string.
    '''
    with open(filepath) as book:
        book_content = book.read()
    return book_content

def main():
    print(get_book_text("./books/frankenstein.txt"))

main()
