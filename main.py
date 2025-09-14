import sys
from stats import *

def bookbot_report(word_count, counts):
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for count in counts:
        c = count["char"]
        if c == ' ' or c == '\n':
            continue
        print(f"{count['char']}: {count['count']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    words = get_word_numbers(path)
    counts = get_char_counts(path)

    bookbot_report(words, counts)
    

    
main()

