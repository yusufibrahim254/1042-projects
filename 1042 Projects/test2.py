import csv
from T040_P1_load_data import book_category_dictionary

book_data = book_category_dictionary('Google_Books_Dataset.csv')

def get_books_by_publisher(name: str, dictionary: dict) ->list:
    """
    Returns  a list of books published by the inputted name and dictionary.
    >>>get_books_by_publisher("DC",'book_data')
    The publisher: “DC”, has published the following books: 
    

    """

    book_lst = []
    cfile = open("book_data", mode='r')
    creader = csv.reader(cfile)
    header = next(creader)
    book_dictionary ={}
    for row in header:
        publisher_name = row[4]
        title = row[1]
        if name == publisher_name:
            book_lst.append(row[1])

    for row in book_lst:
        print('The publisher:', name +', has published the following books:',book_lst)        
  
get_books_by_publisher("DC",'book_data')