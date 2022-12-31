#Yusuf Ibrahim (101231208)

# Exercise 2

def max_min(lst: list) -> list:
    """
    returns a tuple with the maximum and minimum number from the given list of tuples
    >>> max_min([(27, 219, 134, 12), (111, 41, 83, 1), (2, 34, 9, 120)])
    [(219, 12), (111, 1), (120, 2)]
    >>> max_min([(0, 0, 0, 1), (10, 20, 20, 6), (4, 2, 8, 19), (3, 110, 1, 10)])
    [(1, 0), (20, 6), (19, 2), (13, 1)]
    >>> max_min([(1, 3, 5, 9), (11, 13, 15, 17), (19, 21, 23, 25), (151, 101, 321, 41), (320, 72, 124, 313)])
    [(9, 1), (17, 11), (25, 19), (321, 41), (320, 72)]
    """
    newlist = []
    for i in lst:
        max_num = max(i)
        min_num = min(i)
        newlist.append((max_num, min_num))
    return newlist    

# Exercise 4

def sum_y(lst1: set) -> int:

    """ 
    returns the sum of the y coordinate of the coordinates that are given in the list lst1.
    
    >>>sum_y({(110.0, 10.2), (121.2, -12.0), (-178, 116), (-141.4, 22.0)})
    136.2
    >>>sum_y({(69.0, 12), (31, 3), (30, 8), (-72, 6)})
    29
    >>>sum_y({(341.7, 2.9), (6.8, -12.0), (45.5, 48.0)})
    38.9
    """
    
    var = 0
    for z in lst1:
        (x, y) = z      
        var += y
    return var  
