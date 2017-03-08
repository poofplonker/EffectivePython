""" Lesson Eleven: Use zip to process iterators in parallel. """
from itertools import zip_longest
NAMES = ['CECILIA','LISA','MARIE']
LETTERS = [len(n) for n in NAMES]

# Lets get the name that is longest.
# We can do this using an index in parallel.
print("Range version")
max_name = ""
max_length = 0
for i in range(len(NAMES)):
    if LETTERS[i] > max_length:
        max_name = NAMES[i]
        max_length = LETTERS[i]
print("Max Name: %s, Max Length: %s" % (max_name, max_length))

# Well thats cool, but it looks pretty noisy. What about enumerate?

print("Enumerate version")
max_name = ""
max_length = 0
for i, letter_count in enumerate(LETTERS):
    if letter_count > max_length:
        max_name = NAMES[i]
        max_length = letter_count
print("Max Name: %s, Max Length: %s" % (max_name, max_length))

# Thats still a bit noisy. What we really want to do is get rid of all
# the indexes. We can do this by using ZIP, which iterates in parallel and
# returns a tuple.

print("Zip version")
max_name = ""
max_length = 0
for name, count in zip(NAMES, LETTERS):
    if count > max_length:
        max_length = count
        max_name = name
print("Max Name: %s, Max Length: %s" % (max_name, max_length))

# This is really nice, but there is a problem with zip:
NAMES.append("CHARLOTTE")
print("Names:")
for name in NAMES:
    print(name)
print("Doesn't handle different length iterators:")

max_name = ""
max_length = 0
for name, count in zip(NAMES, LETTERS):
    if count > max_length:
        max_length = count
        max_name = name
print("Max Name: %s, Max Length: %s" % (max_name, max_length))

# You can use ziplongest in itertools. This has a "Fillvalue", which
# returns if the other iteration is longer.
max_name = ""
max_length = 0
for name, count in zip_longest(NAMES, LETTERS, fillvalue=9):
    if count > max_length:
        max_length = count
        max_name = name
print("Max Name: %s, Max Length: %s" % (max_name, max_length))
