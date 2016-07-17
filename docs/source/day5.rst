Day 5: Collections and Loops
=============================

Take home work
-------------

1. Play with the turtles more. On Monday, we will have a vote on who has the best design or coolest turtle.
	- you should also be practicing your for loops!
	- take the numbers out of the loops by replacing them with variables
	- having is so that the variables are set at the top of the file
	- then you can change the variables in one place and change the behavior!
2. Put multiple turtles into a list and use a for loop over that list to do the same thing to multiple turtles at once!
3. Play the guessing game using a while loop.
	- The computer guesses a number
	- The user has to guess until they are right
	- The computer tells the user higher or lower
	- The computer counts how many guesses it took
4. Play with the following code, using your own options. You could even add more lists!
::
	import random
	adjectives = ["super", "silly", "evil", "furry"]
	nouns = ["rabbit", "tortiose", "gorilla"]
	keep_going = True
	while keep_going:
	   pick1 = random.choice(adjectives)
	   pick2 = random.choice(nouns)
	   print("you are a {} {}".format(pick1, pick2))
	   answer = input("Keep going? (yes/no) ")
	   keep_going = answer == "yes"
	   # alternate version:
	   # keep_going = (input("Keep going? (yes/no) ") == "yes")
	print("goodbye!")



Review
------

Collections
***********

Collections are variable types that can hold more than one value - not just an int or a String, but a *sequence* of values. We learned about three types: Lists, Tuples, and Dictionaries.

**Lists** in Python are simply that - a linear, ordered bunch of values. Lists can have ints, Strings, booleans, etc., for their members. You can make an empty list like this: 
::
	grocery_list = list()
	
Or, you can make one like this:
::
	grocery_list = []
	
Finally, you can make a list that already has items in it:
::
	grocery_list = ["bread", "milk", "beans"]
	
You can get items from a list using the same syntax as indexing and slicing strings (see Week 02 for a refresher). For example, ``grocery_list[0]`` will return the String "bread", and ``grocery_list[1:]`` will return ["milk", "beans"]. Notice how when you return just one item, the type is whatever the item was - a String, int, etc. But if you get multiple elements, it's just a shorter List.

- Reassign List items: ``grocery_list[1] = "bacon"``
- Add an item to the end of a List: ``grocery_list.append("butter")``
- Delete a particular item: ``del grocery_list[1]``	
- Get the length of a list: ``len(grocery_list)``

**Dictionaries** in Python work like real-world dictionaries; instead of organizing items by number, each item gets a "key", and you can look up items by their "key." Dictionaries are great for when you want to store information and don't care about how it's ordered - you just want to be able to look up specific entries by name.

To make a blank dictionary and add items to it:
::
	my_dict = {}
	my_dict["first entry"] = "This is the first entry!"
	my_dict["second entry"] = "This is the second entry!"

Then, ``print(my_dict["first entry"])`` will print "This is the first entry!"

The values in a Dictionary can be Strings, Ints, Booleans, anything! The keys can be Strings, Ints, or Tuples.

**Tuples** in Python are very much like Lists. The main difference is that the items in a tuple can't be changed once they've been set. Tuples are useful for when you have a set of values that you know won't change, and don't want to allow the program to change.

To make a Tuple:
::
	num_tuple = (0, 1, 2)

If you try ``num_tuple[1] = 5``, Python will complain.

While Loops
***********
A ``while`` loop is another kind of loop - it works differently than a ``for`` loop. ``while`` loops have two parts: a ``<condition>``, and a body of code. When Python reaches a ``while`` loop, it checks to see if ``<condition>`` is True. If it is, the code in the code body will be executed. 

Once that's finished, Python will again check ``<condition>``. If it's True, the code will execute again, and again, and again...This continues until ``<condition>`` is False. So be careful - a ``while`` loop can continue forever if ``<condition>`` never becomes False!

Syntax of a ``while`` loop:
::
	x = 5
	while x < 10:
		print("The loop is still going!")
	print("Looks like the loop finished!")

The above is an example of an **infinite loop**. x never gets changed, so it'll *always* be less than 10. The final line will never be reached!

Bonus
*****
Finally, we learned a cool trick with ``for`` loops and Collections (list, dictionary, etc.) All of these are examples of **iterables** - objects in Python that you can loop over by taking the first item, and then the next, and the next, etc.

And you can use any iterable in a for loop - it doesn't just have to be ``range(x)``! Check out the following example:
::
	grocery_list = ["olive oil", "eggs", "ham", "celery"]
	for item in grocery_list:
		print("Remember to buy: ")
	print("That's it!")
	
The above code will output:
::
	Remember to buy: olive oil
	Remember to buy: eggs
	Remember to buy: ham
	Remember to buy: celery
	That's it!

Random
******

The random library lets you do randomized events.  You must always start with importing it. 

For example:
::
	import random
	# num is short for number
	num = random.random()
	
You can do random integers and random choices too:
::
	import random
	num = random.randint(0,10)
	
	pet_names = ["euclid", "fido", "bob"]
	selected_name = random.choice(pet_names)

With the ``random.randint(start,stop)``, the integer sampled is just like ``range``: it will only go UP to the stop number. It will never include it. 



Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1M1iEGW40-onThVBWCQ3dv7x4NrWbBaiunDtQCNUESkg/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>