""" Lesson Eight: Avoid using more than two expressions in a list comp"""

# Using nested expressions in list comprehensions is fine if you are
# straightforward.
MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Flat Matrix: ", [y for x in MATRIX for y in x])

#This is also not too complicated.
SQUARED = [[x**2 for x in y] for y in MATRIX]
print("Squared Matrix: ", SQUARED)

SATAN_MATRIX = [[[x] for x in y] for y in MATRIX]
print("Satan Matrix: ", SATAN_MATRIX)

#If you were triple nested, it would just be more simple to split into loops.
flat = []
for z in SATAN_MATRIX:
    for y in z:
        flat.extend(y)

print("Flattened Satan Matrix: ", flat)

# You can have a list comprehension with ifs and ands:
A = list(range(10))
print("Evens over 4 with double if:", [x for x in A if x > 4 if x % 2 == 0])
print("Evens over 4 with and:", [x for x in A if x > 4 and x % 2 == 0])

# A loop or double condition or triple conditions or single loop with
# double condition is too much. If you do this, then just use a helper function
# with a loop.
