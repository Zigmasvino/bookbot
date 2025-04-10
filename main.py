from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    # it takes a filepath as input and returns the contents of the file as a string
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def print_book_report(file_path):
    # it takes a filepath as input and returns the contents of the file as a string
    text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {get_number_of_words(text)} total words ")
    print("--------- Character Count -------")
    for leter in get_sorted_list_of_dictionaries(get_number_of_characters(text)):
        if leter[0].isalpha():
            print(f"{leter[0]}: {leter[1]} times")
            
    print("============= END ===============")


def main():    
    print_book_report(sys.argv[1])
  
main()
