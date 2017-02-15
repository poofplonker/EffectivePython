""" Lesson Five: Know how slicing works """

# Interestingly, you can slice any python class that has __getitem__
# and __setitem__.

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("First Four", A[:4])
print("Last Four", A[-4:])
print("Middle Three", A[4:-4])

#Leave out leading 0 and final index at end because they are redundant.
#This is also more readable.
assert A[:5] == A[0:5]
assert A[5:] == A[5:len(A)]

print("Everything", A[:])
print("First Five", A[:5])
print("All but Last One", A[:-1])
print("Everything but First Four", A[4:])
print("Last Three", A[-3:])
print("Two, Three, Four", A[2:5])
print("Everything but First Two and Last One", A[2:-1])
print("Last Three Without Last One", A[-3:-1])

#Slicing also means you can slice to things outside the boundary Without
#Raising an exception.

print("First Twenty Items: ", A[:20])
print("Last Twenty Items: ", A[-20:])

#When you slice, you get a COPY of the list.
#So A[:] is an idiom for copying a list.

B = A[:]
B[7] = 8
print("A:", A)
print("B:", B)

# You can also replace a slice of a list with a different length thing
# and it will slice that assignment in. But it must be an iterable, not
# a simple value.

B = A[:]
B[4:8] = [5]
print("B Sliced Assignment B[4:8] = 5", B)

# if you assign A[:] then it replaces the current list, rather than making a
# copy.

A[:] = [1, 2, 3]
print("Oh no more list", A)

#PYLINT PERFECT
