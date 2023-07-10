#!/usr/bin/python3
'''
   This module has a class that inherits from list in task-0
'''


class MyList(list):
    '''A custom list class that inherits from the built-in list class.

    Public Methods:
        Print_sorted() - Prints the list elements in sorted order.
    '''
    def print_sorted(self):
        '''
        Prints the list, but sorted(ascending sort)
        '''
        print(sorted(self))
