from T040_P1_load_data2 import book_category_dictionary

dictionary = book_category_dictionary('google_books_dataset.csv')


def get_books_by_category(data_dict: dict, category: str) -> int:
    """
    Returns the number of books in the category parameter found within a dictionary.
    
    >>>get_books_by_category(dictionary, "Fiction")
    The category Fiction has 39 books. This is the list of books:
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2 : The Painted Man (The Demon Cycle. Book 1) by Peter V. Brett
    Book 3 : Edgedancer: From the Stormlight Archive by Brandon Sanderson
    etc.
    >>>get_books_by_category(dictionary, "Superheroes")
    The category Superheroes has 5 books. This is the list of books:
    Book 1 : Spider-Man: Anti-Venom by Dan Slott
    Book 2 : Watchmen (2019 Edition) by Alan Moore
    Book 3 : Spider-Verse: Volume 1 by Dan Slott
    Book 4 : Young Justice Vol. 1 by Art Baltazar
    Book 5 : Immortal Hulk Vol. 1: Or Is He Both? by Al Ewing
    >>>get_books_by_category(dictionary, "Science Fiction")
    The category Science Fiction has 0 books.
    """
    category_books = data_dict.get(category)
    book_count = 0
    title_list = []
    author_list = []
    if category_books != None:
        for book in category_books:
            book_count += 1
            title_list += list([book.get("title")])
            author_list += list([book.get("author")])
        print("The category", category, "has", book_count, "books. This is the list of books:")
        for title in title_list:
            print("Book",title_list.index(title)+1,":", title, "by", author_list[title_list.index(title)])
    else:
        print("The category", category, "has", book_count, "books.")
    return book_count

def get_books_by_rate(data_dict: dict, rate: int) -> int:
    """
    Returns the number of books with a rating within the range of the parameter plus 1.
    Inclusive the lower limit and exclusive upper limit.
    
    >>>get_books_by_rate(dictionary, 2)
    There are 0 books whose rate is between 2 and 3. This is the list of books:
    >>>get_books_by_rate(dictionary, 3)
    There are 8 books whose rate is between 3 and 4. This is the list of books:
    Book 1 : Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2 : Bring Me Back by B A Paris
    Book 3 : Mrs. Pollifax Unveiled by Dorothy Gilman
    etc.
    """
    book_count = 0
    category_list = list(data_dict.values())
    title_list = []
    author_list = []
    for book_list in category_list:
        for book in book_list:
            book_data = list(book.values())
            if book_data[2] != "N/A":
                if book_data[2] >= rate and book_data[2] < (rate + 1):    
                    if not book_data[0] in title_list:
                        book_count += 1
                        title_list.append(book_data[0])
                        author_list.append(book_data[1])
    print("There are", book_count, "books whose rate is between", rate, "and", str(rate + 1)+". This is the list of books:")
    for title in title_list:
        print("Book",title_list.index(title)+1,":", title, "by", author_list[title_list.index(title)])
    return book_count

#get_books_by_category(dictionary, "yuh")
#get_books_by_rate(dictionary, 2)