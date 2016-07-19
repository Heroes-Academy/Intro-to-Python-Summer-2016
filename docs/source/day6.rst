Day 6: Basic Functions
======================

Take Home Work
--------------

You should practice while loops, for loops, and writing your own functions.

1. Write a while loop menu.
	- At the start of the while loop, show the user the menu
	- then, after they select an option, do whatever that option does
	- Finally, ask them if they want to do another thing
	- The goal is to have a loop we will combine with Problem 2. 
	- So, just for testing, make a joke menu like in previous assignments.
2. Write turtle functions for the menu
	- Write the following functions.
	- In the while loop menu, have them be options
	- If you want, you could have sub options.
	- For example, if one of the menu options was to have the turtle draw a square, then the submenu option could be having the user input the size of the square.
::
	def spiral(someturtle, loop_count, angle):
		''' the loop count is for the range and the angle is for the spiral turning '''
	
	def polygon(someturtle, number_of_sides, side_length):
		''' remember that the turning angle for any polygon is 360 / number_of_sides '''
	
	def turtle_profile1(someturtle):
		''' come up with some settings for a turtle. this can include speed, shape, and color 
			assign those settings to the turtle here
		'''

	def turtle_profile2(someturtle):
		''' come up with some more settings for a turtle. this can include speed, shape, and color 
			assign those settings to the turtle here
		'''
3. Finish drawing the face with turtles


Review
------

This week we talked about **functions** - what they are, what're used for, and how to write our own.

Function Basics
***************
So what is a function? The short answer is, it's a bunch of lines of code that you set aside - kind of like a special *paragraph* - and give a name to. Then, anywhere else in your code, you can use that same name to execute the function's code, without having to type it all out again. Just by using the name, the computer will know what code you're talking about.

Here's an example: Say you wrote some code that prints a bunch of sentences in a particular order, like this:
::
	print("First sentence\n")
	print("Second sentence\n")
	print("Final sentence!\n")
	
If you wanted to write this code as a **function**, it would look like this:
::
	def three_sentences():
		print("First sentence\n")
		print("Second sentence\n")
		print("Final sentence!\n")

Things to note:
- ``def`` (define) is a keyword that tells Python you're about to write a function
- The next word is the name of the function (you choose this - it can be whatever you like), followed by parentheses (these also indicate to Python that it's a function)
- The line ends with a colon, just like loops and ``if`` statements. As always, the contents of the function - its "paragraph" - are indented by 4 spaces

Defining Functions and Calling Functions
****************************************
The code above just **defines** the function called ``three_sentences``. None of the code will actually be executed; we;re just letting the computer know that in the future, if we say ``three_sentences()``, we're talking about this paragraph.

After you've **defined** the function like we did above, you can **call** it anywhere in your code. Calling a function is the same as executing a function. You can call a function simply by writing the function name, followed by parentheses. For example, look at this code block:
::
	def three_sentences():
		print("First sentence\n")
		print("Second sentence\n")
		print("Final sentence!\n")
	
	print("OK, let's call the function!\n")
	
	three_sentences()
	
The final line of code actually calls the function. Once a function has been defined, you can call it as many times as you want! You can also define as many functions as you want in a single program. 


Function Arguments
******************

The function above is really simple - you just call it, and it does something. Some functions, like ``print()``, are different - you *need* to put something in the parentheses, because it's expecting something to be in the parentheses.

The thing you put in the parentheses is called an **argument**. That's just another word for the input of a function.

We can write functions that take arguments too. For example, let's say you wanted to write a function where, when somebody calls it, they need to put a name (probably a String) in the parentheses, and the function will print out a greeting for that particular person. It would probably look something like this:
::
	def greeting(name):
		print("Hello there, " + name + "!\n")

To write a function that takes an **argument** in its parentheses, you simply write a *variable name* inside the parentheses like I did with the ``name`` variable above. Then you can use that variable in the function! 

Now, when you call the ``greeting()`` function, you need to put something in the parentheses, like this:
::
	greeting("Penny")
	greeting("Emerald")
	greeting("Cortana")
	
If you try to just call ``greeting()``, Python will complain, because when you *defined* the function, you told it to expect something in the parentheses.

Python doesn't check which type of variable an argument is, so even if you're expecting a String, someone could still type ``greeting(5.127849)`` without crashing the program.

You can even have more than one argument in a function! Check out the example below:
::
	def add_two_numbers(num1, num2):
		sum = num1 + num2
		print(sum)
		print("\n")
		
If you put that at the top of your program, now you can call it to get the sum of any two numbers! For example, try ``add_two_numbers(0, 5)``, ``add_two_numbers(100, -56)``, and ``add_two_numbers(.0456, .55903)``. s you can see, multiple arguments are just separated by commas, both when **defining** a function, and also **calling** a function.


Scope
*****

We briefly discussed this in class - just a little warning to keep in mind when working with functions. In our ``add_two_numbers(num1, num2)`` function above, ``num1`` and ``num2`` are the arguments that the functions expects. They're both variables that we can use within that function's *paragraph*. 

However, outside the paragraph, if you try to reference ``num1`` and ``num2``, Python will complain that it doesn't know what variables you're talking about. This is because ``num1`` and ``num2`` **only** exist within the function's paragraph. 

So, for example:
::
	def add_two_numbers(num1, num2):
		sum = num1 + num2
		print(sum)
		print("\n")
		
	print("Let's sum two numbers!")
	add_two_numbers(1, 2)
	print(num1)
	
...will crash, because of the last line. We'll talk more about scope later on.

We finished up by experimenting with turtles and writing functions. Check the Extra Resources section after tomorrow to see some examples!


Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1YB9yRWOYtxk0AsyE_Niq1L04Qxaa6XjsHuhpGgLI-hk/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
