""" Lesson Four: Write Helper functions instead of Complex Expressions
"""

# I feel like im starting to get a good handle on this one, but lets run through
# the code anyway.

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))
print(type(my_values))

#how would I convert these all to numbers?
my_values_copy = my_values.copy()
for key_temp, value in my_values_copy.items():
    my_values_copy[key_temp] = [int(z) for z in value if z.isdigit()]

print(repr(my_values_copy))
# This is not quite right - becuase an invalid field just becomes blank.

# The book recommends a syntax like this. Remember we also need something that
# queries values that aren't there.

# What this logic does is uses get to grab the value, which is a list with
# a string in it, or return a list with an empty string if nothing is there.
#Then, the string in that list is extracted, and evaluated to false or true,
# depending on whether it is empty. If it is empty, its false and we get a zero,
# otherwise we get the string.

#We also need to cast the result to int.
red = int(my_values.get('red', [''])[0] or 0)
green = int(my_values.get('green', [''])[0] or 0)
opacity = int(my_values.get('opacity', [''])[0] or 0)
print('Red:     %r' % red)
print('Green:     %r' % green)
print('Opacity:     %r' % opacity)

#This is already primed for better factoring anyway.

# In this situation, the play is to use IF else to break out the logic over
# several lines, making the code easier to read.

red = my_values.get('red', [''])
if red[0]:
    red = int(red[0])
else:
    red = 0

# But what is much better is to write a helper function.

def get_first_int(values, key, default=0):
    """ Helper function to strip numbers from query string."""
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    print('%s:      %r' % (key.title(), found))
    return found

result = get_first_int(my_values, 'red')
result = get_first_int(my_values, 'green')
result = get_first_int(my_values, 'opacity')

# There is a temptation to slam everything into one line in python because
# you can, but when you put something into a helper function you get the benefit
# of compactness by calling on the function and the readability when you have
# to look at how the thing works.
