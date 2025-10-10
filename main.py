
def main():
    book_path = ("./books/frankenstein.txt")
    file_contents = get_book_text(f"{book_path}")
    print(file_contents)

def get_book_text(book_path):
    file_contents = ""
    with open(book_path) as file:
        file_contents = file.read()
    return file_contents

main()