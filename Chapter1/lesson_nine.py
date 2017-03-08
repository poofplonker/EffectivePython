""" Lesson 9: Prefer generators to lists when comprehensions are large"""

# The problem with list comprehensions is that they make a copy of the list.
# This is fine if the input is small, but if it is large this copy eats memory.


FILE_TO_READ = '/Users/cinnamonscudworth/Programming/EffectivePython/Chapter1/lesson_six.py'
VALUE = [len(x) for x in open(FILE_TO_READ)]
print("Line Length of lesson 7:", VALUE)


# A generator a something that evaluates to an iterator that yields one item
# at a time from the expression.

VALUE_IT = (len(x) for x in open(FILE_TO_READ))
print(next(VALUE_IT))
print(next(VALUE_IT))

# One of the nice things about iterators is that you can compose them.
VALUE_IT = (len(x) for x in open(FILE_TO_READ))
VALUE_IT_2 = ((x,x**0.5) for x in VALUE_IT)
print(next(VALUE_IT_2))
print(next(VALUE_IT_2))

# This is very fast, but the problem is that generators are stateful, so you
# need to be careful.
