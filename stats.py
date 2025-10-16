import re

WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*")

def get_book_text(path):
    with open(path, encoding="utf-8") as file:
        return file.read()

def tokenize_words(text):
    return WORD_RE.findall(text)

def get_num_words(path):
    text = get_book_text(path)
    return len(tokenize_words(text))

def get_char_count(path):
    text = get_book_text(path).lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_dictionary(char_count):
    char_list = []
    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    char_list.sort(key=sort_on, reverse=True)
    return char_list

