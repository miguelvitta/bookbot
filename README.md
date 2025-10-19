# BookBot

**BookBot** is a Python program that analyzes the text of a book and provides:

* The **total number of words** in the book.
* A **frequency count of all alphabetical characters**, sorted from most frequent to least frequent.

It is designed to help understand the structure and composition of any text file in a simple and easy-to-read report.

---

## Features

* Counts words in a book using a **simple whitespace-based approach**.
* Counts characters **case-insensitively** and ignores non-alphabetical characters in the final report.
* Outputs a clean, human-readable report to the console.
* Supports analyzing **any text file** by passing the file path as a command-line argument.

---

## Project Structure

```
BookBot/
│
├── main.py           # Entry point of the program
├── stats.py          # Contains all functions for reading, tokenizing, counting, and sorting
├── books/            # Folder containing text files to analyze
│   └── frankenstein.txt
└── README.md         # This file
```

---

## Functions Overview

**stats.py** contains:

* `get_book_text(path)` – Reads the full text of a book.
* `get_num_words(path)` – Counts total words in a book.
* `get_char_count(path)` – Returns a dictionary of character frequencies.
* `sort_dictionary(char_count)` – Converts character frequency dict to a sorted list of dictionaries with `{"char": ..., "num": ...}`.
* `sort_on(item)` – Helper function for sorting by count.

---

## How to Run

1. Make sure you have **Python 3 installed**.
2. Open a terminal and navigate to the project folder.
3. Run the program by passing the path to a text file:

```bash
python3 main.py ./books/frankenstein.txt
```

---

## Sample Output

```
============ BOOKBOT ============
Analyzing book found at ./books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
...
============= END ===============
```

---

## Notes

* The program ignores non-alphabetical characters in the **character frequency report**.
* Word counting is based on **splitting on whitespace**, so hyphenated words (e.g., “mother-in-law”) count as one word.
* You can analyze any `.txt` file by providing its relative or absolute path.
