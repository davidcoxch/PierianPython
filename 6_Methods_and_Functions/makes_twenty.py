"""
From 03-Function Practice Exercises.ipynb notebook
MAKES TWENTY: Given two integers, return True if the sum of the integers is 
20 or if one of the integers is 20. If not, return False

makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""


def makes_twenty(a,b):
    return a + b == 20 or 20 in (a,b)


print(makes_twenty(10,20))

print(makes_twenty(12,8))

print(makes_twenty(2,3))
