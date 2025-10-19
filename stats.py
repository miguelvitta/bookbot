def get_book_text(path):
    with open(path, encoding="utf-8") as file:
        return file.read()

def get_num_words(path):
    with open(path, encoding="utf-8") as file:
        file_contents = file.read()
    words = file_contents.split()
    return len(words)

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

