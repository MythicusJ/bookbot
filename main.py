import sys

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

from stats import count_words, count_chars, char_counts_sorted


def main():
    if len(sys.argv) != 2: 
        prog = sys.argv[0]
        print(f"Usage: python3 {prog} <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = count_words(book_text)
    char_dict = count_chars(book_text)
    sorted_chars = char_counts_sorted(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for row in sorted_chars:
        ch = row["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {row['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
