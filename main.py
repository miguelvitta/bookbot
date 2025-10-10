from stats import get_num_words, get_book_text

def main():
    book_path = ("./books/frankenstein.txt")
    # file_contents = get_book_text(f"{book_path}")
    #print(file_contents)
    num_words = get_num_words(book_path)
    print(f"Found {num_words} total words")


main()