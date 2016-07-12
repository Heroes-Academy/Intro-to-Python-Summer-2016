"""
Welcome to this week's bonus problems!

These are a bit harder, so it's fine if you can't get them all. But give them a try and see
what you can do!

I will provide a description of a problem.
It is your job to convert that description into a formula.
Once you've figured out the equation to solve the problem, you must
write code to do the equation!

Each of the problems will require you to get some user input. You can use the input() function like normal.

Here's how you should structure your code:
1. Write an intro print statement explaining the situation for the problem.
2. Then write an input statement to get the relevant information.
3. Finally, use your equation to calculate the answer.
4. Then, print out the answer in a nice way.

I have completed the first one as an example.

When you finish a problem, send me the code you used for it, the input you gave, and what your answer was.
"""

### Luke's Rabbits
# Luke loves his rabbits.
# However, they are multiplying like crazy!
# Currently, he has 7 rabbits. Every month, they double.  So next month, he will have 14.
# Feeding each rabbit costs $10 dollars a month.
#
# The input should be how many months Luke has his rabbits
# The output should be how much money it would cost to feed all of those rabbits that month.


print("""Every month, the number of rabbits doubles.
          If you tell me how many months you want to breed the rabbits,
          then I will calculate how much money it will cost in food""")
num_months = int(input("Number of months: "))

# since it doubles every month, then 7 * 2  is the first month, 7 * 2 * 2 is the second
# so, it is 7 * 2 ** num_months
num_rabbits = 7 * 2 ** num_months
food_cost = 10*num_rabbits
print("It will cost you", food_cost, "dollars to feed your rabbits that month")


### Bill's Money
# Bill wants to know how much money he can earn from saving.
# He has an investment account that gives him 10% every month
# He wants to know how much month he will have after 1, 3, and 6 months
#
# The input should be how much money he wants to invest.
# The output should be how much money he will have after 1, 3, and 6 months


### Sara's Army
# Sara wants to hire an army.
# It will cost her $500 per soldier.
#
# The input should be the amount of money that Sara has
# The output should be the number of soldiers she can get.
#
# Note that the amount of money she has may not be exactly the amount of a soldier
# For example, if she has $700 dollars, she can only get 1 soldier, and will have some money left over. That's fine!
# So, you will have to do floor division. (do you remember how to do this?)
# See the slides if you forgot how
