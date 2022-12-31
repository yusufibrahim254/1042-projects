# Function initially written by: Bradley Taylor - 101228342

# Reviewed by: 
#Sophia Verma - 101224612
#Jasmine Wong - 101240501
#Yusuf Ibrahim - 101231208

def book_category_dictionary(filename: str)->dict:
    """
    Returns a dictionary of books based on their category when given the file
    name as input.
    >>> print(book_category_dictionary('google_books_dataset.csv'))
    >>> {'Fiction': [{'Title': "Antiques Roadkill: A Trash 'n' Treasures Mystery",
                       'Author': 'Barbara Allan',
                       'Rating': '3.3', 'Publisher': 'Kensington Publishing Corp.', 
                       Length': '288 pages', 'Language': 'English'},
                       etc.
    >>> dictionary = book_category_dictionary('google_books_dataset.csv')
    >>> print(dictionary['Comics'])
    >>> {'Title': 'Deadpool Kills the Marvel Universe',
         'Author': 'Cullen Bunn',
         'Rating': '4.2',
         'Publisher': 'Marvel Entertainment',
         'Length': '96 pages',
         'Language': 'English'}
         Etc.
    
    """
    file = open(filename, 'r')
    first_line = True
    word_list = []
    category_dictionary = {}
    
    for line in file:
        word_list = line.strip('\n').split(',')
        if first_line == True:
            first_line = False
            header = word_list
        else:   
            if word_list[2] == 'N/A':
                dictionary_entry = [{header[0]:word_list[0], header[1]:word_list[1], header[2]:
                                    word_list[2], header[3]:word_list[3], header[4]:
                                    word_list[4], header[6]:word_list[6]}]
            else:
                dictionary_entry = [{header[0]:word_list[0], header[1]:word_list[1], header[2]:
                                    float(word_list[2]), header[3]:word_list[3], header[4]:
                                    word_list[4], header[6]:word_list[6]}]                
            
            if word_list[5] in category_dictionary:
                category_dictionary.update({word_list[5]: category_dictionary.get(word_list[5]) 
                                            + dictionary_entry})
            else:
                category_dictionary.update({word_list[5]:dictionary_entry})
                 
    file.close()
    return category_dictionary

dictionary = book_category_dictionary('google_books_dataset.csv')
#print(dictionary)
