from stats import get_char_occurences, get_num_words, sort_occurences


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_occurences = get_char_occurences(book)
    sorted = sort_occurences(char_occurences)
    for line in sorted:
        char: str = line["char"]
        if char.isalpha():
            print(f"{char}: {line['num']}")


main()
