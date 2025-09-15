from stats import count_words, count_char, sort_counted_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    print("============ BOOKBOT ============")

    # check args
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    
    filepath = sys.argv[1]

    print(f"Analyzing book found at {filepath}...")

    contents     = get_book_text(filepath)
    words        = count_words(contents)
    chars        = count_char(contents)
    sorted_chars = sort_counted_chars(chars)

    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['count']}")
    
    print("============= END ===============")

main()
