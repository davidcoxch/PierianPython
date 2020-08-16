"""
From 03-Function Practice Exercises.ipynb notebook
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False
"""

def animal_crackers(text):
    list = text.split()
    
    return list[0][0] == list[1][0]


print(animal_crackers('Levelheaded Llama'))

print(animal_crackers('Crazy Kangaroo'))