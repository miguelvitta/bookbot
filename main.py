
def main():
    book_path = ("./books/frankenstein.txt")
    # file_contents = get_book_text(f"{book_path}")
    #print(file_contents)
    num_words = get_num_words(book_path)
    print(f"Found {num_words} total words")


def get_book_text(book_path):
    file_contents = ""
    with open(book_path) as file:
        file_contents = file.read()
    return file_contents

def get_num_words(book_path):
    num_words = []
    file_contents = ""
    with open(book_path) as file:
        file_contents = file.read()
    num_words = file_contents.split()
    return len(num_words)

main()