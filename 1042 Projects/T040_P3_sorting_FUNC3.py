# Jasmine Wong 101240501

# Imported modules
from typing import List
from T040_P1_load_data import book_category_dictionary

book_data = book_category_dictionary('Google_Books_Dataset.csv')

# Function definitions
def sort_books_author(dataset: dict) -> List[dict]:
    """
    Returns a list of books sorted in alphabetical order by author name. Books by 
    the same author are sorted alphabetially by book title. List returned contains 
    dictionaries with each dictionary containing information for one book.
    >>>sort_books_author(dictionary)
    [{'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from 
    the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay',
    'rating': 4.7, 'publisher': 'Pan Macmillan', 'pages': '112', 'language': 'English', 
    'category': ['Humor']}, {'title': 'And Then There Were None', 'author': 'Agatha 
    Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': '224', 
    'language': 'English', 'category': ['Fiction', 'Detective', 'Thrillers', 'Mystery']}, etc
    """
    lst = []
    for key in dataset.keys():
        data = dataset.get(key)
        for book in data:
            if lst == []:
                category_dict = {"category": list([key])}
                book.update(category_dict)
                lst += list([book])
            if lst != []:
                title_lst = []
                for book_in_lst in lst:
                    title_lst += list([book_in_lst.get("title")])
                if book.get("title") in title_lst and lst[title_lst.index(book.get("title"))].get("category") != list([key]):
                    book_in_lst = lst[title_lst.index(book.get("title"))]
                    category_lst = book_in_lst.get("category") + list([key])
                    category_dict = {"category": category_lst}
                    lst.pop(title_lst.index(book.get("title")))
                    book.update(category_dict)
                    lst += list([book])
                if not book.get("title") in title_lst:
                    category_dict = {"category": list([key])}
                    book.update(category_dict)
                    lst += list([book])
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j].get("author") == lst[j+1].get("author"):
                if lst[j].get("title") > lst[j+1].get("title"):
                    lst[j+1], lst[j] = lst[j], lst[j+1]
            elif lst[j].get("author") > lst[j+1].get("author"):
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst

a = sort_books_author(book_data)
print(a)
