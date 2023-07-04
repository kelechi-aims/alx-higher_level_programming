#!/usr/bin/python3
'''
   A class LockedClass with no class or object attribute.
'''


class LockedClass:
    '''
    LockedClass prevents dynamic creation of instance attibutes
    except for 'first_name'.
    '''
    __slot__ = ("first_name",)

    def __setattr__(self, attr, value):
        '''
        Override the __setattr__ method to prevent
        creation of instance attribute.

        Only allow assignment to the 'first_name' attribute.
        Raise an AttributeError for other creations.
        '''
        if attr != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(attr)
                    )
            self.__dict__[attr] = value
