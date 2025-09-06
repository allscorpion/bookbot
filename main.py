from stats import amount_of_words, amount_of_characters, sorted_characters
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
    

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_name = sys.argv[1]
    contents = get_book_text(book_name)
    num_words = amount_of_words(contents)
    characters = amount_of_characters(contents)
    sorted = sorted_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if (item["char"].isalpha()):
            print(f"{item["char"]}: {item['num']}")
    print("============= END ===============")

main()