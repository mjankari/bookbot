import sys
from book import Book

def check_arguments():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return arguments[1]

def main():
    filepath = check_arguments()
    document = Book(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {document.get_filepath()}")
    print("----------- Word Count ----------")
    print(f"Found {document.count_words()} total words")
    print("--------- Character Count -------")
    for char_dict in document.count_characters():
        char = char_dict["character"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()
