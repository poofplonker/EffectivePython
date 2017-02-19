""" Lesson 7: Use list comprehensions rather than map() and filter()"""

A = list(range(10))

# The fact you can filter list comprehensions makes them easy to use.
print("Squares: ", map(lambda x: x**2, A))
EVEN_ONLY_LC = [x**2 for x in A if x % 2 == 0]
print("Sqaures even only: ", EVEN_ONLY_LC)

#You can do this by chaining a filter, but it looks complex:

EVEN_SQUARES_MF = map(lambda x: x**2, filter(lambda x: x % 2 == 0, A))
assert EVEN_ONLY_LC == list(EVEN_SQUARES_MF)
print("Assertion Succeeded")

# Also, is that filter being applied before the map?
# If you remove evens, you remove all even squares.

B = list(range(4))
NOT_THREE_SQUARES = list(map(lambda x: x**2, filter(lambda x: x != 3, B)))
print("Not Three Squares: ", NOT_THREE_SQUARES)

# It is applied before.

# Dictionaries can also be list comprehended.

EXAMPLE_DICT = {'Things': 1, 'OtherThing' : 2, 'Indeed' : 3}
print("Example Dictionary: ", EXAMPLE_DICT)
INVERTED_DICT = {rank: name for name, rank in EXAMPLE_DICT.items()}
print("Inverted Example: ", INVERTED_DICT)
print("Name Lengths as Set: ", {len(name) for name in EXAMPLE_DICT.keys()})
print("Name Lengths: ", [len(name) for name in EXAMPLE_DICT.keys()])
