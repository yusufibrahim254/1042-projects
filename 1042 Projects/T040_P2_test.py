# Bradley Taylor - 101228342 #

# Functions 3 & 4

# Imports #

from unit_testing import check_equal
from T040_P1_book_category_dictionary import book_category_dictionary
from T040_P2_fun_3_4 import get_books_by_category
from T040_P2_fun_3_4 import get_books_by_rate

# Functions #

# Main Script #

dictionary = book_category_dictionary('google_books_dataset.csv')

print('Testing: get_books_by_category')
check_equal('get_books_by_category(dictionary, "Fiction")', get_books_by_category(dictionary, "Fiction"), 39)
check_equal('get_books_by_category(dictionary, "Superheroes")', get_books_by_category(dictionary, "Superheroes"), 5)
check_equal('get_books_by_category(dictionary, "Science Fiction")', get_books_by_category(dictionary, "Science Fiction"), 0)
print('\n')

print('Testing: get_books_by_rate')
check_equal('get_books_by_rate(dictionary, 2)', get_books_by_rate(dictionary, 2), 0)
check_equal('get_books_by_rate(dictionary, 3)', get_books_by_rate(dictionary, 3), 8)
print('\n')
