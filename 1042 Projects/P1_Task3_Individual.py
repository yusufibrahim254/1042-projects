import string
from typing import List

# Function Definitions
def book_list(filename: str)-> dict:
    '''
    returns a list with the title, author, language, rating, publisher, category, and number of pages with the book data stored in a dictionary with the provided file name.
    >>>book_list(google_books_dataset.csv)
    {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
    "author": " Barbara Allan",
    "language ": "English",
    "rating": 3.3,
    "publisher": " Kensington Publishing Corp.",
    "category": " Fiction",
    "pages": 288},
    {"title": "The Nightshift Before Christmas: Festive hospital
    diaries from the author of million-copy hit",
    "author": " Adam Kay",
    "language": "English",
    "rating": 4.7,
    "publisher": "Pan Macmillan",
    "category": " Biography ",
    "pages": 112,
    },
    {another element},
    '''
    file = open(filename, "r")
    book_attributes = ['title','author','rating','publisher','pages','category','language']
    book_list = []
    counter = 0

    for line in file:
        current_book = {}
        line.strip() 
        book_content = line.split(',') 
        if counter > 0: 
            for i in range(len(book_attributes)):
                current_book.update({book_attributes[i]:book_content[i]}) 
            book_list.append(current_book)
        counter += 1

    file.close()

    return book_list

file = "google_books_dataset.csv"
