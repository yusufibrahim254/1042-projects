# Originally coded by Ayman Kamran 101232406
# Reviewed by: Taimur Meraj 101211320, Makayla McMurray 101194095, Edward Lancaster 101183206

#import statements

#from T106_P1_book_category_dictionary 
#import book_category if put into a folder 

#Function definition

def book_category(in_file:str) -> list:
    """
    Returns books name and its specifications when function is called
    
    >>>book_category("google_books_dataset.csv")
    {'Fiction': [{'title:': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author:': 'Barbara Allan', 'language: ': 'English', 'rating:': 3.3, 'publisher:': 'Kensington Publishing Corp.', 'pages:': '288'}]}
    
    
    {'Fiction': [{'title:': 'The Painted Man (The Demon Cycle. Book 1)', 'author:': 'Peter V. Brett', 'language: ': 'English', 'rating:': 4.5, 'publisher:': 'HarperCollins UK', 'pages:': '544'}]} 

    
    {'Fiction': [{'title:': 'Edgedancer: From the Stormlight Archive', 'author:': 'Brandon Sanderson', 'language: ': 'English', 'rating:': 4.8, 'publisher:': 'Tor Books', 'pages:': '226'}]} 
    
    """
    
    in_file = open("google_books_dataset.csv", "r")
    book_dictionary = {}
    val_dict = ['title', 'author', 'rating', 'publisher', 'page', 'language']
    for book in in_file:
        bookdict = {}
        book = book.strip()
        book = book.split(",")
        current_category = book[5]
        if "category" not in book:
        
       
            if book[2] != 'rating' and book[2] != 'N/A':
                book[2] = float(book[2])

            for i in range(len(val_dict)):
                bookdict.update({val_dict[i]:book[i]})
                                
            if book[5] not in book_dictionary:
                book_dictionary.update({book[5]:[]})
            book.pop(5)
            book_dictionary[current_category].append(bookdict)
            
    in_file.close()

    
    return book_dictionary
    
    


#Main Script

print(book_category("google_books_dataset.csv"))
        