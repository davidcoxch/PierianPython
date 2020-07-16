# Set of examples for boolean's (True/False)

a = 2 > 3
print(a)

b = 3 <= 2
print(b)

c = 3 == 2.0
print(c)

d = 3.0 == 3
print(d)

e = 4**0.5 != 2
print(e)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# It is false because l_one[2][0] is 3 and l_two[2]['k1'] is 4
f = l_one[2][0] >= l_two[2]['k1']
print(f)