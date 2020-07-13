# We will use indexing in various ways

# Given the string 'hello' give an index command that returns 'e'

a = 'hello'[1]
print("The letter with index value 1 is:")
print(a)
print()

# Reverse the string 'hello' using slicing:

b = 'hello'[::-1]
print("Hello reveresed with slicing looks like:")
print(b)
print()

# Given the string 'hello', give two methods of producing the letter 'o' using indexing.
c = 'hello'[4]
d = 'hello'[-1]

print("In hello, you can use indexing to print out 'o' using hello[4]:")
print(c)
print()

print("In hello, you can use indexing to print out 'o' using hello[-1] to reverse the order:")
print(c)
print()
