# ECOR1042
# T-40
# Sophia Verma 101224612

import string
import T040_P1_load_data # Importing dataset dictionary

# Get Book by Title
def get_books_by_title(dataset:dict, title:str) -> bool:
    """Returns if a book has been found in the dataset by it's title.
    >>> getbook["Antiques Roadkill: A Trash 'n' Treasures Mystery"]
    >>> "The book has been found"
    >>> True
    """
    for key in dataset.keys(): # Looking at the keys of the dataset
        data = dataset.get(key) # Getting all keys
        for book in data:
            if book['title'] == title: # Getting the values for the key 'title'. (Obtaining book data from title)
                print("The book has been found")
                return True
    print("The book has NOT been found")
    return False
        

def get_books_by_author(dataset:dict, author:str) -> str:
    count = 0
    """Returns the number of books written by the author as well as the title and rating.
    >>> get_book["Barbara Allan"]
    >>> The Author Barbara Allan has published the following books:
    >>> Book 1: "Antiques Roadkill: A Trash 'n' Treasures Mystery", rate: 3.3
    >>> Book 2: "Antiques Con", rate: 4.8
        Etc.
    >>> get_book["Adam Kay"]
    >>> The Author Adam Kay has published the following books:
    >>> Book 1: "Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt", rate: 4.7
    """
    repeat = []
    print("The author", author, "published the following books:")
    for key in dataset.keys(): # Getting all keys
        data = dataset.get(key)
        for book in data:
            if book['author'] == author and not (book['title'] in repeat): # Getting the values for the key 'author', making sure it equals to the inputted author, and eliminating repeats.          
                repeat.append(book['title']) # Add repeats to another list
                print("Book {}:".format(count+1), (book['title']+"{}".format(",")), "rate:", book['rating'])
                count += 1  # Count each book
    return count


#get_author = get_books_by_author(T040_P1_load_data.dictionary, "Barbara Allan")

#get_title = get_books_by_title(T040_P1_load_data.dictionary, "Antiques Roadkill: A Trash 'n' Treasures Mystery")
#print(get_title)

