Week 09: Application
====================


Summary
^^^^^^^

We spent the entire lesson working on final projects. In case you forget, the project description and list of requirements are available in the lecture slides below. We'll be presenting final projects next week - the first half of the class will be spent wrapping up and debugging the projects, and the second half will be the actual presentations.

We also learned how to do a few new things that could spice up the final project.

  - Play .wav sound files in Python
  - Generate random numbers
  - Move a Turtle object using the arrow keys


Play Sound Files in Python
**************************

(this method will only work on Windows computers!)

We covered two methods of doing this. First, if you simply download a sound file and leave it on your computer somewhere, you'll need to give Python the location of the sound file. For example, let's say I'm playing a sound file called "rocket_ship.wav", located in ``C:\Users\Public\Downloads`` on my computer. To play that, you'd use the following code:
::
  import winsound, sys
  
  winsound.PlaySound("C:\\Users\\Public\\Downloads\\rocket_ship.wav", winsound.SND_FILENAME)
  
Let's break down the code above. You import ``winsound``, a Python library that can play sounds on a Windows computer, and ``sys``, which lets Python perform operations on the file system (such as opening and closing files).

The ``winsound.PlaySound`` function actually opens and plays the sound file - we give a String for the first argument, which is the location of the sound file - remember to include the file name and extension! (``.wav`` in this case) Remember that in order to write a backslash (\) in a Python string, you need to use a double-backslash. Otherwise, it may think you're trying to use a special String symbol, such as ``\n`` or ``\t``. 

For the second argument, we tell Python that that String was just the name of a sound file. That way, the program knows to look in that location, open the file, and play it.

Alternatively, you can put the sound file right in your PyCharm project folder. If you do, you don't need to supply the full path to the file - you can just use the filename (Python will check the project folder for it). The code would look like this:
::
  import winsound, sys
  
  winsound.PlaySound("rocket_ship.wav", winsound.SND_FILENAME)
  
This also makes it easier to move your code onto a different computer - you can just copy the whole project folder, sound file included.


Generate Random Numbers
***********************

Generating random numbers in Python is easy! Look at the following sample code:
::
  import random
  
  x = random.randint(0, 10)
  print(x)
  
This code will print a random number from 0 to 10.

Move a Turtle Object Using the Arrow Keys
*****************************************
You can use the following code to set up a Turtle object and move it with the arrow keys:
::
	import turtle
	
	bob = turtle.Turtle()
	
	# set the speed at which Bob turns and moves forward/backward
	move_speed = 10
	turn_speed = 10

	# functions that will be called by the arrow keys
	def move_turtle_forward():
	  bob.forward(move_speed)

	def move_turtle_backward():
	  bob.backward(move_speed)

	def turn_turtle_left():
	  bob.left(turn_speed)

	def turn_turtle_right():
	  bob.right(turn_speed)

	# don't have Bob draw a line as he moves about the screen
	bob.penup()
	bob.speed(0)
	bob.home()

	# with this code, when the user hits the designated key on the keyboard, the specified function will be called
	screen.onkey(move_turtle_forward, "Up")
	screen.onkey(move_turtle_backward, "Down")
	screen.onkey(turn_turtle_left, "Left")
	screen.onkey(turn_turtle_right, "Right")
	
	# this continually has the program wait for the user to hit keys on the keyboard
	screen.listen()

	turtle.done()

That's it! The explanations for the code are included in its comments. 

Homework
^^^^^^^^

Next week, for the final lesson, you'll be presenting your project to the class. For each project, we'll do three things:

  - You'll provide a brief overview of your project to the class
  - We'll run through the project a few times, testing various input choices and seeing what happens
  - We'll all look through the code together to see how it works

For homework, apart from having your project ready (or mostly ready - you will have an hour at the start of class to finish it), you'll need to put together your project overview. I've provided an example in the "Extra Resources" section below. It's really short - just three slide or so, to give us a general idea of what your project is and what it does.

At a minimum, the overview should include:

  - What your project is about and what it's supposed to do
  - Whether it's complete, or if not, what features are missing
  - A few things you learned while working on the project
  - One or two things you could do to expand it in the future
  
Remember to email me with any questions about either your final project or the overview!

Extra Resources
^^^^^^^^^^^^^^^

`Project Overview Example <https://github.com/Heroes-Academy/Intro-to-Python-Spring-2016/blob/master/code/Week%2009/Project%20Overview%20Example.pdf>`_


Lecture Slides
^^^^^^^^^^^^^^

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1TzKzBXEwWhcGWkrB5iCGHLtRLQwjU_tBs44HicrH2mk/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
