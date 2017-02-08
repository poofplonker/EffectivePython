"""
Lesson Three: Bytes, Strings, and Unicode
"""
from __future__ import print_function
# Python3 has bytes and strings. Bytes contain 8 bit values -
# strings are unicode.

#Python 2 has str, which is raw 8 bit values, and unicode has unicode.


# So unicode is great, because due to the characters corresponding to a 16 bit
# integer you can represent all these different characters. However, this is
# quite often not space efficient, so people ENCODE the sequence of integers
# in a unicode string in different ways. This has to do with compression,
# and which byte is read first in a unicode char, and so on and so forth.
# So the way a unicode string is represented in a machine can vary.

# If you run this in python2, you get a syntax error,
# because there is no encoding.
try:
    unicode_string = u'This is \xc3mlaut'
    bytes_string = 'This is umlaut'
    idk_string = u'Lets see whats happening hereé'

except UnicodeDecodeError:
    print("Well you didn't get a syntax error, \
        but you need to have ascii in initial string")
except SyntaxError:
    #can I even catch this?
    print("Can't specify a string in this way")

# Ok, so as long as we use u'' and then only ordinal characters, we can punch
# in a unicode string.

# Without specifying the u'', we get UnicodeDecodeError. Decoding is changing
# raw bytes to an string encoding, so what we are doing is punching in a bytewise
# representation.

# So the recommendation is that you work in unicode internally and deal with
# encodings at the furthest boundary of the programme.

# So when you specify a default in python 2 its bytes.

# Python 2
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of unicode


print(to_unicode(unicode_string))
print(to_unicode(bytes_string))
print(to_unicode(idk_string))

# Python 2
def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of str

# The problem with python2 is that when unicode only contains ascii then it
# behaves like str() (bytes). SO you can concatenate and yaya.
conv_idk_string = to_unicode(idk_string)
concat = conv_idk_string + unicode_string

#different types, seems fine
concat2 = idk_string + unicode_string

concat3 = unicode_string + idk_string
print(concat)

#In python3, file read and write, unless specified, is done by strings.
# In python2 its done by bytes. So if you want to write to a file whcih isn't
# opened in binary, you need to convert it to a string. 
