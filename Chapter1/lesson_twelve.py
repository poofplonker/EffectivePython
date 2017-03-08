""" Lesson Twelve: Don't use else after a loop """

# Python has syntax where you can put an else after a loop.

for i in range(3):
    print(i)
else:
    print("Whats going on here?")

# This executes after the main body of the loop executes, which begs the
# question as to why it is different than any other typical statement after
# the loop.

# Here else means : do this if the block above didn't happen. This means that
# if you break the loop, you don't get the else.

print("Breaking on 2")
for i in range(3):
    print(i)
    if i ==2:
        break
else:
    print("Whats going on here?")

#but if you iterate over an empty sequence, the else will immediately run -
# as well as when you iterate over something false.

for x in []:
    print(x)
else:
    print("Ending after an empty sequence")

# Basically, the design of this syntax is for iterating over a set of options
# where you exit if something succeeds or fails. If no such thing happens,
# then you declare something to happen. This is an example when you have coprime
# numbers:

print("Coprime test of 4 and 9")
A = 4
B = 9
for i in range(2, min(A, B)+1):
    if A % i == 0 and B % i == 0:
        print("Not coprime")
        break
else:
    print("Coprime")

# But what you really want to do is one of either two styles in a smaller
# function:

# A return release:

def coprime(a,b):
    for i in range(2, min(A, B)+1):
        if A % i == 0 and B % i == 0:
            print("Not coprime")
            return False
    print("Coprime")
    return True

# Or if you need more complicated logic,
# a variable.

# Use a simple loop, not the else statement. 
