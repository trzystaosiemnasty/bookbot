def get_num_words(book: str) -> int:
    return len(book.split())


def get_char_occurences(book: str) -> dict[str, int]:
    occurences = {}
    for char in book:
        c = char.lower()
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1
    return occurences


def sort_occurences(dictionary: dict[str, int]) -> list[dict]:
    items = []
    for key in dictionary:
        items.append({"char": key, "num": dictionary[key]})
    items.sort(reverse=True, key=sort_on)
    return items


def sort_on(items: dict) -> int:
    return items["num"]
