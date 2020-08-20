"""
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24

"""

def multiply(numbers):
    ct = 1

    for x in numbers:
        ct = ct * x

    print(ct)

multiply([1, 2, 3, -4])
