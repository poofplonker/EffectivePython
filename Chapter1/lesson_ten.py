""" Lesson Ten: Prefer Enumerate over Range"""

FLAVOUR_LIST = ['PEACH','LEMON','VANILLA']
# You can iterate over a list naturally.

print("Old Style")
i = 1
for flavour in FLAVOUR_LIST:
    print("Flavour %s: %s" % (i, flavour))
    i += 1

print("Enumerate Style")
# That is C-style, but if you use enumerate() you can get the index as well.
for i, flavour in enumerate(FLAVOUR_LIST):
    print("Flavour %s: %s" % (i+1, flavour))

# You can even make this better by optionally giving an option to enumerate
# of where to stop or start counting.

print("Enumerate Optional")
for i, flavour in enumerate(FLAVOUR_LIST, 1):
    print("Flavour %s: %s" % (i, flavour))
