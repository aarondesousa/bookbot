import sys
from stats import (
    get_num_words, 
    get_char_counts,
    sort_chars_by_count
)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # dict instead of list
    # for key in sorted_chars:
    #     if key.isalpha():
    #         print(f"{key}: {sorted_chars[key]}")

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_chars = sort_chars_by_count(char_counts)

    print_report(book_path, num_words, sorted_chars)

main()
