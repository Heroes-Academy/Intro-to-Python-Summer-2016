"""
 Exercise 4
 Random Loopy practice

 Use random to simulate 2 6-sided dice rolls for as many times as a user wants.

 Procedure:
    Rolling the dice:
     1. Ask the user for a number, this will be the total number of rolls
     2. Use a for loop and inside each for loop, roll two dice
     3. Count the number of pairs
    
    Reporting the numbers:
     1. Calculate the ratio of the number of times pairs came up and the total number
        - This ratio is also called the empirical probability
        - It is the percentage of time that we saw the pairs
     
    Repeating experiments with your code:
     1. Run your code a couple of times. You'll notice the number can change each time.
     2. Increase the dice rolls. Does the ratio start to converge? 
        - In other words, does the ratio start to become stable rather than changing?
    
 Reflection:
     1. What happens if the user increases the dice roll number?
     2. What number does it become?
"""

import random

dice_one = random.randint(0,6)

