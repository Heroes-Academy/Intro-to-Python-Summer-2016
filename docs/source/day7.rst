Day 07: More Functions and Intro to Minecraft
=============================================

Review
------

Below is review information for Minecraft, Functions that return results, and classes.

If you are looking to install the minecraft libraries, check here:  :doc:`installminecraft`

Minecraft Overview
******************

Primarily, you can do the following things with the library

1. Move the player
2. Get the player's location
3. Set blocks
4. Get block information

There are many things you can do with this. 

**Resources and Links**

1. `A list of the commands you can do with mcpi <http://www.stuffaboutcode.com/p/minecraft-api-reference.html>`_
2. `The Learn to program with Minecraft book <https://www.nostarch.com/programwithminecraft>`_


Functions with Return Statements
********************************
Last week, we only talked about functions that take input arguments and print things. But what if we wanted to write a function that returns a value you can put in a variable?

The answer is a **return** statement. At the end of a function, use a return statement to have the function spit out a particular value. Then, when you call that function, you can put the returned value in some variable. 

Here's an example:
::
	def addition_func(x, y):
		result = x + y
		return result

Then, if you want to call this function, you can do this:
::
	the_sum = addition_func(10, 15)
	
We call the function, and put the return value into the ``the_sum`` variable.

Python Classes
**************
Finally, we learned the basics of defining and using our own custom-made object classes. The basic idea behind **defining** a class is that you're writing a recipe for a particular type of object. you can think of it like this: if you have a room full of chairs, each of those chairs is a chair object, but "chair" would be the name of the class. 

After you've defined a class (written your recipe), you can use it to make copies of your custom-made object in code. The Lecture Slides have example code in case you forget!

See the "Extra Resources" section for examples. In short, the proper syntax is this:
::
	class <Class_Name>:
		property_a = value_a
		property_b = value_b
		property_c = value_c
		
		def some_class_function(self)
			<code>
			<code>
			<code>
			
Remember, classes have two very important features in Python: **properties**, which are details about the object that describe it, and **functions**, which are things that the object can **do**. 

For example, a ``Dog`` object in Python might have the properties ``name``, ``age``, ``height``, etc., and functions like ``run(self)``, ``bark(self)``, and ``fetch(self)``. Remember that when you're defining functions inside an object, you need to make the first argument (the first thing in the parentheses) the keyword ``self``, which tells Python, "this function belongs to this object type." 

Similarly, inside of a class's function, if you want to reference one of that class's properties, you also need to use the ``self`` keyword. So, in the ``bark(self)`` function for a dog, if you wanted to print its name, it would look like this:
::
	def bark(self)
		print("Hello! My name is " + self.name)

Don't forget the ``self`` keyword!


Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1NN_ABGEUyzSj3ntAICFilRvRDkJhXz7qn75RWlCI5uE/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
