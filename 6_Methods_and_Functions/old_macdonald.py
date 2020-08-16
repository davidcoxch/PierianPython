"""
From 03-Function Practice Exercises.ipynb notebook
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
old_macdonald('macdonald') --> MacDonald
Note: 'macdonald'.capitalize() returns 'Macdonald'
"""

def old_macdonald(text):
    first = text[0:3].capitalize()
    second = text[3::].capitalize()
    return first + second

print(old_macdonald('macdonald'))