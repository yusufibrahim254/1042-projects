# Yusuf Ibrahim - 101231208

from unit_testing import check_equal
from T040_P1_load_data import book_category_dictionary
from T040_P2_add_book import add_book
from T040_P2_remove_book import remove_book

book_data = book_category_dictionary('google_Books_Dataset.csv')



# Funciton 1


def check_equal(description: str, outcome, expected) -> int:
    """
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.
    
    Parameters "outcome" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      outcome, str(outcome_type).strip('<class> ')))
        return 0
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
        return 1
    else:
        print("{0} PASSED".format(description))
        return 1
    print("------")

# Main Script

def main():
    """
    Returns the number of tests passed and tests failed for the following call examples
    """
    # Three tests for each function, so for example get_books_by_title should test three different examples
    # Therefore twenty-four tests in total
    count = 0
    TF = 0
    count += check_equal("Testing add book", get_books_by_title(dictionary, "Antiques Roadkill: A Trash 'n' Treasures Mystery"), True)
    TF += 1
    count += check_equal("Testing book by author", get_books_by_author(dictionary, "Barbara Allan"), 4)
    TF += 1
    print("Test passed", count)
    print("Test failed", TF - count)

if __name__ == '__main__':
    main()