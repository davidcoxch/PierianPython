"""

Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons

"""

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1 = str1.replace(" ", "")
    str1 = str1.lower()
    str1 = set(str1)
    alphabet = set(alphabet)
    return str1 == alphabet


print(ispangram('The quick brown fox jumps over the lazy dog', alphabet=string.ascii_lowercase))