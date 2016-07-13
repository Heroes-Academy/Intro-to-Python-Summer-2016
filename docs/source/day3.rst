Week 3: Booleans, If-Elif-Else, For
===================================

Summary
-------

To come after class.


In-Class and Homework Exercises
-------------------------------

1. Turtle Designs
	- Draw a face
	- Draw your initials
	- Draw something creative
		+ The class will vote tomorrow on who's is the best!
2. Inputs and Menus!  
	- Make a userid
	- a basic menu with a joke
	- a two-level menu with two jokes!
	- Make your own menu
3. Break things!
	- Make reproducible code! 
	- This means making the python file and creates the error
	

Review
------

Booleans
********
Booleans are variables that can have a value of ``True`` or ``False``. 
You can set Boolean variables in code with something like ``x = True``, or you can use **comparison operators.** 

These are the comparison operators we discussed:

- < less than
- > greater than
- <= less than or equal to
- >= greater than or equal to
- == equal to (remember, in Python, "equal to" uses two equals signs, because one equals sign is just used for making a variable)
- != not equal to

Comparison operators compare the values of two different variables, and will evaluate to either True or False. 
For example, ``5 > 3`` will evaluate to ``True``, but ``10 == 9`` will evaluate to ``False``. 
You can use these to make Boolean variables as well.

Booleans can also be combined using the ``and`` and ``or`` keywords. 
If ``x`` and ``y`` are Booleans, the expression ``x and y`` will only be ``True`` if both ``x`` and ``y`` are ``True``. 
``x or y`` will only be ``True`` if at least one of them is ``True``. 
And of course, ``not x`` will just be the opposite of ``x``.

We practiced evaluating Booleans using cards and complex conditions (suite == hearts and not number <= 5).

If Statements
*************

``if`` statements are comprised of two ingredients: a condition (which must evaluate or be a boolean), and some code. 
Python checks if the condition is True; if it is, the code will be executed.
But if the condition is False, Python will just ignore the code and move on.

If statements kind of resemble a paragraph - the condition goes at the top, and the accompanying code is all indented by 4 spaces.
::
	if <condition>:
		do some code
		do some more code
	back to normal code
	
The computer knows when the ``if`` statement paragraph ends because the indentation stops. 
That's the only way it will know!

If-Elif-Else
************

More complex types of ``if`` Statements: ``if-else``, and ``if-elif-else`` structures.

It helps to think of the three of them like this:

- An ``if`` statement gives the computer one option: if ``<condition>`` is True, then do something. That's all.
- An ``if-else`` statement gives the computer two options: if ``<condition>`` is True, then do something. If ``<condition>`` is False, do some other thing!
- An ``if-elif-else`` statement gives the computer several options, where you can say "Check all of these conditions until you find one that's True."

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
		
You can put in however many  "elif" portions you want. The computer will just go through each of the conditions, one after another, until it finds one that's True. 
Then, it will skip the rest of the paragraph. And if none of the conditions are True, it will do whatever is written under the "else" section.


For Loops
*********

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

For loops can be tricky to wrap your head around. The best thing to do is to use the above two examples, copy them into PyCharm, and verify that they work. 
Then try changing the number in range(), and also change around what happens in the indented text. 
The best way to practice new coding techniques is to try it yourself


Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1tjpvWrhVX4e_gsURvMK6TqGiaevVJyKow5zxLD6YyA0/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


Trinkets
--------

1. Turtle Loops 1

.. raw:: html

    <iframe src="https://trinket.io/embed/python/eb7b608d56" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

2. Turtle Loops 2

.. raw:: html

    <iframe src="https://trinket.io/embed/python/fc826fce5d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

3. Turtle Circles

.. raw:: html

    <iframe src="https://trinket.io/embed/python/6db31dcde4" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

4. Turtle Triangle Trick!

.. raw:: html

    <iframe src="https://trinket.io/embed/python/abd2f8c9d6" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

5. Two Turtles and Triangle Stamps

.. raw:: html

    <iframe src="https://trinket.io/embed/python/999e0b531e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

6. Turtle Star!

.. raw:: html

	<iframe src="https://trinket.io/embed/python/59941a36dd" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
	


Extra Turtle Challenge: Specific Coordinates
--------------------------------------------

Turtles are awesome because we can make them do many things.
Let's create the turtle first:

.. code-block:: python
   :linenos:

    import turtle
    bob = turtle.Turtle()
    bob.speed('fastest')

Now,  in the following, we can make the turtle go to very specific coordinates:

.. code-block:: python
   :linenos:

    bob.setpos(100,0)

Bob is now at x=100 and y=0.
In general, the syntax is ``setpos(x_coord,y_coord)``.

We can use this to make interesting things.
For example, if I want to make bob do a triangle without a for loop:

.. code-block:: python
   :linenos:

    bob.setpos(-100, 0)
    bob.setpos(0,100)
    bob.setpos(100,0)
    bob.setpos(-100, 0)

What's even cooler is that we can use variables to make this scalable:

.. code-block:: python
   :linenos:

    tri_size = 30
    bob.setpos(-1*tri_size, 0)
    bob.setpos(0, 1*tri_size)
    bob.setpos(1*tri_size, 0)
    bob.setpos(-1*tri_size, 0)

But this is a lot of code for something simple.
What if we could store all of the coordinates ahead of time and then
use a for loop to loop over the coordinates?

.. code-block:: python
   :linenos:

    tri_size = 130
    coords = [[-1, 0], [0, 1], [1, 0], [-1, 0]]
    for coord in coords:
        x = coord[0]
        y = coord[1]
        bob.setpos(x*tri_size, y*tri_size)


This triangle looks a little funny.
What if we wanted to have each side be the same length AND use the coords list?
What numbers would we have to change?

The Challenge
*************

Use a coordinate list like the one above to make your initials (first and last).