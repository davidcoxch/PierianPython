"""
Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as
v = 4/3 * 3.14 * r(cubed) 
"""

def vol(rad):
    return (4/3) * 3.14 * (rad**3)

print(vol(2))