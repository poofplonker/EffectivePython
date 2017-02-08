""" Lesson Two of Effective Python: Follow the Style guide """

# Highlighted Hints:
# Imports at the top!
import standard_module

import third_party_module

from . import own_module
# Use spaces not tabs!

# Lines should be not be longer than 80 characters. Good thing we have the line

# Continuations of lines should be indented one level after original level.

#example_tuple = ('This', 'Line',' Is Getting Too Long then we need to ',
#    'Continue on the next line.')

#wow, this needs 13 more spaces ?!?

#Constants should be UPPER_CASE_UNDERSCORE style
#One space before and after assignment

OTHER_TUPLE = ('This', 'Line', 'Is Getting Too Long then we need to ',
               'Continue on the next line.')

# Hrmm.

# Functions and Classes should be separated by two lines
# In a class, methods should be separated by one line.

# Class methods should take the parameter cls first
# Instance methods should take self.

# Classes should take the CapitalizedWord Style
# functions variables and attributions should be lower_underscore style
class ExampleClass(object):
    """Class Docstring Yo"""
    def example_class_function(cls):
        """Function docstring indeed"""
        pass

    def instance_function1(self):
        """Function docstring indeed"""
        pass


class OtherClass():
    """Class docstring indeed"""
    pass

#No spaces for .... Indexing:
result = OTHER_TUPLE[1]

#Function Calls:
result = sorted(OTHER_TUPLE)

#This file has 13 pylint violations. Use pylint!
