# Yusuf Ibrahim - 101231208

from T040_P1_load_data import dictionary
from T040_P2_add_remove_search_dataset import *

def user_interface ():
    user_interface = False
    while True:
        
        print("1- L)oad data")
        print("2- A)dd book")
        print("3- R)emove book")
        print("4- Q)uit")
        
        print()
        user_input = input ("Enter your command:")
        
        if user_input == "L" or user_input == "l":
            dictionary = input("Enter the dictionary file name:") 
            dictionary
            user_interface = True
            
        elif user_interface == False:
            print ("No file loaded")
            print()
            
        else:
            
            if user_input == "A" or user_input == "a":
                title = input ("Enter title:")
                author = input ("Enter author's name:")
                publisher = input ("Enter publisher's name:")
                rating = input ("Enter rating:")
                page_count = input ("Enter page count:")
                category = input ("Enter category:")
                language = input ("Enter language:")
                a = add_book(book_category_dictionary(dictionary), (title, author, rating, publisher, page_count, category, language))
                print(a)
                
                    
            elif user_input == "R" or user_input == "r":
                title = input ("Enter title:")
                category = input ("Enter category:")
                b = remove_book(book_category_dictionary(dictionary), title, category)
                print(b)
               
                    
            elif user_input == "Q" or user_input == "q":
                break
                
            else: 
                print("Invalid command")
                print()

user_interface()
