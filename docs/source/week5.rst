Week 5: Collections and Loops
=============================

Summary
-------

We covered a lot of material this week. This recap will be important for getting the homework done!

Topics:

- Review of ``for`` loops
- Review of If-Elif-Else structure

See the page for Week 04 for a review of those two topics.

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

And that brings us to the end of the lesson!


Homework
--------
For homework this week, you'll write 3 different files in PyCharm. Email each to me when you've finished them! You can either email the file itself, or just copy and paste your code into the email. My address is tmeo@njgifted.org 

Remember, ask questions if you have any difficulty! These three assignments are a good way to tell if you've really got the basics down, which is important this far into the class.

Practicing with Lists
*********************
Make a list that uses different types of variables for its items (use ints, booleans, and strings). It should be at least 5 items long.

After you make the list, ask the user to enter a number. Print out the **type** of the item at that index in the list. (Do you remember how to do this? If you've forgotten, try using Google!) 

A word of caution - like we saw in class, if the index number is too high, the program will run into an error! Use an ``if/else`` statement to check if the number they gave is too high. If it is, just print a message telling the user they should have picked a smaller number, and move on.

Finally, use a ``for`` loop to print out each item in the list individually.

Practicing with Dictionaries
****************************
Pick 5 random words, either from a physical dictionary or using Google. Make a Python dictionary whose keys are the words, and whose values are the definitions (you can keep the definitions short). 

At the end of the program, ask the user to enter one of the words in your dictionary. Print out the definition of the word they chose, using you Python dictionary.

Something to think about: What happens if the user types in a word that isn't in your dictionary yet? Try it out - we'll see how to deal with this in a future lesson...

Practicing with While Loops
***************************
Have a variable x that starts at 0, and another to represent an upper limit. Repeatedly ask the user for a number, and increase x by that amount. 

Keep asking for numbers until x has risen above the upper limit you chose. At the end, print out what the final value of x is - and tell the user whether it's even or odd (hint: you'll have to use one of the math operators...)

Extra Resources
---------------


Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1uv27qr6qiAJppnXoqVAgrKq54PAyaVTUzEFVU15j388/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>