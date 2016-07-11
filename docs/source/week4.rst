Week 4: Turtles, Elif-Else, and For Loops
=========================================


Summary
^^^^^^^

This week we learned more complex types of If Statements: The If-Else, and If-Elif-Else structures.

It helps to think of the three of them like this:

- An If statement gives the computer one option: if ``<condition>`` is True, then do something. That's all.
- An If-Else statement gives the computer two options: if ``<condition>`` is True, then do something. If ``<condition>`` if False, do some other thing!
- An If-Elif-Else statement gives the computer several options, where you can say "Check all of these conditions until you find one that's True."

Each kind of statement is indented in the same way - with 4 spaces. Here's an example of each:

If Statement:
::
	if x == 5:
		print("x is 5!")
		
If-Else Statement:
::
	if x == "Penny":
		print("Your name is Penny!")
	else:
		print("Looks like your name isn't Penny!")
		
If-Elif-Else Statement:
::
	if age == 50:
		print("You're really old!")
	elif age == 20:
		print("You're kind of young!")
	elif age == 10:
		print("You're a kid!")
	else:
		print("I wonder how old you are?")
		
You can put in however many  "elif" portions you want. The computer will just go through each of the conditions, one after another, until it finds one that's True. Then, it will skip the rest of the paragraph. And if none of the conditions are True, it will do whatever is written under the "else" section.

We talked about the concept of Objects in Python. A Turtle is an example of a Python Object. You can make a Turtle, show a turtle on-screen, move it around, print out information about it, etc. 

More specifically, Objects have two qualities: **functions,** which are things that the object can *do*, and *properties,* which are pieces of information that describe an object.

Every different type of Object has its own unique set of functions and properties. For example, a Turtle Object has the functions ``forward()``, ``left()``, ``right()``, etc. Notice how functions always end in parentheses!

We'll talk more about Objects later - and eventually you'll learn how to write your own! - but for this week, I just wanted to introduce the concept. Objects are **things**, functions are **actions**, and properties are **details** about an Object.

We spent quite a while working with Turtles and doing various activities - drawing shapes and words, using different colors, etc. A link to the Turtles Cheat Sheet I handed out is included in the "Extra Resources" section below, so look there if you want to try some out on your own!

The last thing we learned about is the ``for`` loop. ``for`` loops are great - they use indented lines to form a 'paragraph' (kind of like If statements!) and let you run the code in that paragraph over and over again, as many times as you want!

Say you wanted to print someone's name 10 times (kind of a ridiculous example). The loop would look like this:
::
	for i in range(10):
		print("Cinder")
		
That's it! If you execute this code in Python (easier to type it into PyCharm than the shell), it will print out "Cinder" ten times in a row.

Breaking it down: 

- ``for`` is a special keyword - when Python sees it, it knows we'll be repeating some code
- ``i`` is just a variable, just like ``x`` or ``username``
- ``range(10)`` is the list of all numbers from 0 to 9

In the above For loop, Python will repeated the indented code 10 times, and each time, ``i`` will take a new value.

- First time through: ``i`` is ``0``
- Second time through: ``i`` is ``1``
- Third time through: ``i`` is ``2``

etc.

So you can also do something like this:
::
	for i in range(5):
		print(i)

This will print 0, 1, 2, 3, and 4, because the code will execute 5 times, and each time, ``i`` has a different value!

For loops can be tricky to wrap your head around. The best thing to do is to use the above two examples, copy them into PyCharm, and verify that they work. Then try changing the number in range(), and also change around what happens in the indented text. The best way to practice new coding techniques is to try it yourself

Homework
^^^^^^^^

No homework this week! Be ready for next week - we'll be reviewing a lot!

Extra Resources
^^^^^^^^^^^^^^^

`Turtle Cheat Sheet <https://github.com/Heroes-Academy/Intro-to-Python-Spring-2016/blob/master/code/Week%2004/Turtles%20Cheat%20Sheet.pdf>`_

Lecture Slides
^^^^^^^^^^^^^^

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/11AbDeg1zcNH7walf2hUoY7wtH0eqttQCvNvRMM1-qzY/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
