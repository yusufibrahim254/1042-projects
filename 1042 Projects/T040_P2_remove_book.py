# Bradley Taylor - 101228342 #

from T040_P1_book_category_dictionary import book_category_dictionary

def remove_book(dictionary: dict, title: str, category: str)->dict:
    if title in str(dictionary.get(category)):
        for data in dictionary[category]:
            if title in data.get('title'):
                    del data['title']
            
        return dictionary
    
dictionary = book_category_dictionary('google_books_dataset.csv')
#print(dictionary)
dictionary = remove_book(dictionary, "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Fiction')
print(dictionary)