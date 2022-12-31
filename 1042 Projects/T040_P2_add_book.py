from T040_P1_book_category_dictionary import book_category_dictionary

def add_book(dictionary: dict, book_data: tuple):
    """
    Takes a dictionary as a dictionary and a dataset for a new book as a tuple
    with 7 pieces of data in the order of: Title, Author, Rating, Publisher, 
    Pages, Category, Language.
    The function returns the updated dictionary. If there was an error with the 
    entry the function will print 'There was an error adding the book' and 
    return the dictionary that was input.
    >>>
    >>>
    """
    first_line = True
    order = ['Title', 'Author', 'Rating', 'Publisher', 'Pages', 'Category', 'Language']
    if (book_data[0] in dictionary) or len(book_data) != 7:
        print('There was an error adding the book')
        return dictionary
    else:
        header = order        
        if type(book_data[2]) == type(''):
            dictionary_entry = [{header[0]:book_data[0], header[1]:book_data[1], header[2]:
                                book_data[2], header[3]:book_data[3], header[4]:
                                int(book_data[4]), header[6]:book_data[6]}]
        else:
            dictionary_entry = [{header[0]:book_data[0], header[1]:book_data[1], header[2]:
                                float(book_data[2]), header[3]:book_data[3], header[4]:
                                int(book_data[4]), header[6]:book_data[6]}] 
        dictionary.update({book_data[5]:dictionary_entry}) 
    print('The book has been added correctly')
    return dictionary

