'''
Use List Comprehension to create a list of the first letters of every word in the string below:
'''

st = 'Create a list of the first letters of every word in this string'

mylist = []

for x in st.split():
    mylist.append(x[0])

print(mylist)