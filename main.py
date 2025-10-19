from stats import get_num_words, get_book_text, get_char_count, sort_dictionary

def main():
    path = ("./books/frankenstein.txt")
    num_words = get_num_words(path)
    # print(f"Found {num_words} total words")
    char_count = get_char_count(path)
    # print(char_count)
    sorted_dictionary = sort_dictionary(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for word in sorted_dictionary:
        if word["char"].isalpha():
            print(f"{word["char"]}: {word["num"]}")
    print("============= END ===============")

main()