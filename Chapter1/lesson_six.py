""" Lesson Six: Don't use start, end and slice in a single Slice """
from itertools import islice

A = list(range(10))

#We can use the slice stride syntax like this:
print("Even: ", A[::2])
print("Odds: ", A[1::2])

# Seems good right? The problem is that :: can introduce bugs.

# Here's a cool idiom for reversing a string or list:

print("Reversed: ", A[::-1])

#However lets try this with a utf-8 string:
FANCY_STRING = "Thé String".encode('UTF-8')
try:
    print("Reversed UTF-8", FANCY_STRING[::-1].decode())
except UnicodeDecodeError:
    print("Can't reverse \"%s\": We messed with the order of the bytes by " \
        "reversing them!" % FANCY_STRING.decode())

# What would [::-2] correspond to? Well, start at the end and take every second
# after that right?

print("A[::-2] ", A[::-2])

#What about [2::-2] - well, it probably mean start at 2, and take every second
# before that.
print("A[2::-2] ", A[2::-2])

# What if you put a end in this statement?

print("A[6:8:-2]", A[6:8:-2])
print("A[6:2:-2]", A[6:2:-2])

#Uhhh..... what?
print("A[6:2]", A[6:2])

# So using start end with negative slice is fine, but if you do it without
# negative slice you get empty list?

# Preferred style is not to use slice, but rather to use sequentially
# slice then subset. Or you can use islice in collections

# islice is great because if you are subsetting then you need to temporarily
# copy a subset of the list, whcih is a waste. Islice returns a generator,
# so you never have too much memory wasted.

B = list(range(1000))
B_1 = B[::2]
print("Every even element except first and last: ", B_1[1:-1])

print("Same Result: ", list(islice(B, 1, len(B)-1, 2)))
