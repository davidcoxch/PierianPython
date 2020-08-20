"""
Write a Python function that accepts a string and calculates the number 
of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!
"""

def up_low(s):
    up = 0
    low = 0
    for x in s:
        if x.isupper():
            up = up + 1
        elif x.islower():
            low = low + 1


            

    print("Sample String : {}".format(s))
    print("No. of Upper case characters : {}".format(up))
    print("No. of Lower case Characters : {}".format(low))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)