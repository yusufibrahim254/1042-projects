# T040
# Function 0 - Group
# Function 1 - Written by Yusuf Ibrahim 101231208, tested by Sophia Verma 101224612
# Function 2 - Written by Bradley Taylor 101228342, tested by Yusuf Ibrahim 101231208
# Function 3 - Written by Jasmine Wong 101240501, tested by Bradley Taylor 101228342
# Function 4 - Written by Sophia Verma 101224612, tested by Jasmine Wong 101240501

# Imports 
from typing import List
from unit_testing import *

# Function Definitions 

# Function 0
def dictionary_to_list(dictionary: dict) -> List[dict]:
    """
    Takes a dictionary and converts its data into a list. Each element of the list 
    is a dictionary that contains information for a single book.
    >>>dictionary_to_list(dictionary)
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 
    'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 
    'language': 'English', 'category': ['Fiction', 'Detective', 'Mystery']}, {'title': 
    'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 
    4.5, 'publisher': 'HarperCollins UK', 'pages': '544', 'language': 'English', 
    'category': ['Fiction', 'Fantasy', 'Thrillers']}, etc
    """
    booklist = []
    books = 0
    for i in dictionary:
            for n in dictionary[i]:
                    n['category'] = [i]
                    for j in booklist:
                            if j['title'] == n['title']:
                                    j['category'] += n['category']
                                    books += 1
                    booklist.append(n)
    return booklist

    

# Function 1
def sort_books_title (dictionary: dict) -> list:
    """
    returns a list with the book data stored as a dictionary book where the books are sorted alphabetically by title.
    >>>sort_books_title(book_data)
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': '300', 'language': 'English'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '864', 'language': 'English'}, ....... (it does this for the whole dictionary)
    (starts with 'salem's lot because of the appostraphe)
    """
    lst_book = dictionary_to_list(dictionary)
    length = len(dictionary)
    for i in range(length):
        for j in range(0, length-i-1):
            if lst_book[j].get('title') > lst_book[j+1].get('title'):
                lst_book[j], lst_book[j+1] =lst_book [j+1], lst_book[j]
    return lst_book


# Function 2
def sort_books_publisher(dictionary: dict) -> list: 
    """
    Takes a dictionary of books and returns a list of the entries sorted 
    alphabetically by publisher name.
    
    >>>dict1 = {'Sample Category': [{'Title': 'Sample Title', 'Author': 'Sample 
    Author', 'Rating': 'Sample Rating', 'Publisher': 'Sample Publisher', 'Pages'
    : 100, 'Language': 'Sample Language'}], 'best': [{'Title': 'A great title', 
    'Author': 'Bradley Taylor', 'Rating': '5.0', 'Publisher': 'Bradley', 'Pages'
    : 400, 'Language': 'english'}], 'second best': [{'Title': 'title1', 'Author'
    : 'Person', 'Rating': '4.9', 'Publisher': 'C', 'Pages': 70, 'Language': 
    'english'}]}
    
    >>> print(sort_books_publisher(dict1))
    [{'title': 'A great title', 'author': 'Bradley Taylor', 'rating': '5.0', 
    'publisher': 'Bradley', 'pages': 400, 'language': 'english'}, {'title': 
    'B very good title', 'author': 'Bradley Taylor', 'rating': '5.0', 
    'publisher': 'Bradley', 'pages': 400, 'language': 'english'}, {'title': 
    'Title1', 'author': 'Person', 'rating': '4.9', 'publisher': 'C', 
    'pages': 70, 'language': 'english'}, {'title': 'Sample Title', 'author': 
    'Sample Author', 'rating': 'Sample Rating', 'publisher': 'Sample Publisher',
    'pages': 100, 'language': 'Sample Language'}]  
    """
    list_sorted = False
    sorted_list = []
    final_list = []
    ORDER = ['title', 'author', 'rating', 'publisher', 'pages', 'category', 'language']
    pub_list = []
    
    sorted_list = dictionary_to_list(dictionary)
    for loops in range(len(sorted_list)):
        for x in range(len(sorted_list)-1):
            if min(sorted_list[x][ORDER[0]], sorted_list[x+1][ORDER[0]]) != sorted_list[x][ORDER[0]]:
                sorted_list[x], sorted_list[x+1] = sorted_list[x+1], sorted_list[x]
    for books in sorted_list:
        if books not in final_list:
            final_list.append(books)
    sorted_list = []
    return final_list


# Function 3
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
    lst = dictionary_to_list(dataset)
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j].get("author") == lst[j+1].get("author"):
                if lst[j].get("title") > lst[j+1].get("title"):
                    lst[j+1], lst[j] = lst[j], lst[j+1]
            elif lst[j].get("author") > lst[j+1].get("author"):
                lst[j+1], lst[j] = lst[j], lst[j+1]
    return lst


# Function 4 
def sort_books_ascending_rate(dictionary):
        """ Returns the book database by their rating in ascending order.
        >>> sort_books_ascending_rate(dictionary)
        >>> [{'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers',
            'author': 'Edward Fields', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': '320',
            'language': 'English', 'category': ['Economics', 'Business']},
            {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan',
            'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English',
            'category': ['Fiction', 'Detective', 'Mystery']}, {'title': 'How to Understand Business Finance: Edition 2',
            'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'pages': '176',
            language': 'English', 'category': ['Economics', 'Business']}, etc. ]
        """
        dictionary = dictionary_to_list(dictionary)
        for n in dictionary:
                if n['rating'] == 'N/A':
                        n['rating'] = 0
        
        booksort = len(dictionary)
        for t in range(booksort):
                for p in range(0, booksort-1):
                        if dictionary[p]['rating'] > dictionary[p+1]['rating']:
                                dictionary[p], dictionary[p+1] = dictionary[p+1], dictionary[p]
        for n in dictionary:
                if n['rating'] == 0:
                        n['rating'] = 'N/A'
        return dictionary

# Main Script

count = 0
TF = 0

# Testing Function 1
count += check_equal("Testing sort books by title", sort_books_title(sampledict1), [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English', 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '544', 'language': 'English', 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': '226', 'language': 'English', 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English', 'category': ['Fiction']}])
TF += 1

count += check_equal("Testing sort books by title", sort_books_title(sampledict2), [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': '384', 'language': 'English', 'category': ['Legal']}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': '40', 'language': 'English', 'category': ['Traditional']}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': '30', 'language': 'English', 'category': ['Finance']}])
TF += 1

count += check_equal("Testing sort books by title", sort_books_title(sampledict3), [{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '864', 'language': 'English', 'category': ['Epic']}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English', 'category': ['Epic']}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '4544', 'language': 'English', 'category': ['Epic']}])
TF += 1

# Testing Function 2
count += check_equal('Testing sort books by publisher',sort_books_publisher(sampledict1),[{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English', 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': '226', 'language': 'English', 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English', 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '544', 'language': 'English', 'category': ['Fiction']}]) 
TF += 1

count += check_equal('Testing sort books by publisher',sort_books_publisher(sampledict2),[{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': '384', 'language': 'English', 'category': ['Legal']}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': '40', 'language': 'English', 'category': ['Traditional']}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': '30', 'language': 'English', 'category': ['Finance']}]) 
TF += 1

count += check_equal('Testing sort books by publisher',sort_books_publisher(sampledict3),[{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '864', 'language': 'English', 'category': ['Epic']}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '4544', 'language': 'English', 'category': ['Epic']}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English', 'category': ['Epic']}]) 
TF += 1

# Testing Function 3
count += check_equal('Testing sort books by author',sort_books_author(sampledict1),[{'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English', 'category': ['Fiction']}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English', 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': '226', 'language': 'English', 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '544', 'language': 'English', 'category': ['Fiction']}]) 
TF += 1

count += check_equal('Testing sort books by author',sort_books_author(sampledict2),[{'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': '40', 'language': 'English', 'category': ['Traditional']}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': '30', 'language': 'English', 'category': ['Finance']}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': '384', 'language': 'English', 'category': ['Legal']}]) 
TF +=1

count += check_equal('Testing sort books by author',sort_books_author(sampledict3),[{'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English', 'category': ['Epic']}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '864', 'language': 'English', 'category': ['Epic']}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '4544', 'language': 'English', 'category': ['Epic']}]) 
TF += 1

# Testing Function 4
count += check_equal("Testing sort books by rate in ascending order", sort_books_ascending_rate(sampledict1), [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language': 'English', 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '544', 'language': 'English', 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': '226', 'language': 'English', 'category': ['Fiction']}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English', 'category': ['Fiction']}])
TF += 1

count += check_equal("Testing sort books by rate in ascending order", sort_books_ascending_rate(sampledict2), [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': '384', 'language': 'English', 'category': ['Legal']}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': '30', 'language': 'English', 'category': ['Finance']}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'pages': '40', 'language': 'English', 'category': ['Traditional']}])
TF += 1

count += check_equal("Testing sort books by rate in ascending order", sort_books_ascending_rate(sampledict3), [{'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '864', 'language': 'English', 'category': ['Epic']}, {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '4544', 'language': 'English', 'category': ['Epic']}, {'title': 'The Tower of the Swallow: Witcher 6', 'author': 'Andrzej Sapkowski', 'rating': 4.6, 'publisher': 'Hachette UK', 'pages': '400', 'language': 'English', 'category': ['Epic']}])
TF += 1  


print("Test passed", count)
print("Test failed", TF - count)
