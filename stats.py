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