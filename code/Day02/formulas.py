"""
Welcome to your first homework assignment!!

I will provide equations and hints in the comments. You must
write the code that reflects the equations.

I will also specify which variables you should get from user input.
You should write a message indicating what the person is inputting.

Whenever you get user input, you can make up your own numbers. Use easy numbers to check your
math, or use huge numbers to test the power of Python!

I have done the first one for you as an example.

I wrote some code here in PyCharm, but you'll be writing your code in the iPython shell like we
do in class. Once you figure out how to do each formula, just send me the code you typed into the
Python shell, what input you used, and what your answer was.

Bonus hint: remember, when you get user input by using the input() function, it's a String.
If you want to do math with it - convert it to a float!
"""

# this is an import for the pi number
# it is used for your questions below
# type this into the iPython shell first
# if you close out of the shell and re-open it, you'll have to put this in again
# now if you type pi and press Enter in the shell, it will return the number pi!
from math import pi

### Area of a Square
# equation: area = side_length ** 2
# you should get the side length from user input, using the input() function
# this one's already done - if you want to test it, type these lines into the Python shell and try
# it for yourself!
print("I will calculate the area of a square")
side_length = float(input("Please tell me the side length: "))
area = side_length ** 2
print("The area of a the square with side_length", side_length, " is", area)

### Area of a Circle
# equation: area = pi * radius**2
# you should get the radius from user input
# remember to print out a message saying what the area is at the end!


### Volume of a Sphere
# equation: area = 4/3 * pi * radius**3
# you should get the radius from user input
# remember to print out a message saying what the volume is at the end!


### Weight on Pluto
# explanation:
# if we know how much less gravity a planet has,
# then we can actually calculate our weight on that planet.
# for example: pluto has 5% of our gravity, which leads to this
# equation: weight_on_pluto = 0.05 * weight_on_earth
# take the user's weight on earth as input (you can use pounds, kilograms, etc.
# then print out what their weight would be on Pluto


### Bonus
## get an Earth-weight from user input
## using that weight, calculate the weights for the other planets
## this is a bonus question - go for it if you want a challenge!!
# Mercury has 38% of our gravity
# Venus has 90%
# The Moon has 16%
# Mars has 38%
# Jupiter has 236%
# Saturn has 108%
# Uranus has 80%
# Nepture has 112%
