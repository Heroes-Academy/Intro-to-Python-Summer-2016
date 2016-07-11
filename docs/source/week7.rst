Week 07: Advanced Functions and Basic Classes
=============================================

Summary
-------

Important Note: No class next week! Don't come in on Sunday, May 29th. Week 08 resumes on Sunday, June 5th.

This was our final week of all-new material! We covered 2 topics: functions that have **return** statements, and an intro to Python **classes**. Short summary below - more information can be found in the lecture slides.

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


Extra Resources
---------------

These are the classes you guys wrote in this week's lesson. Use them as an example!

The ``Clown`` class:
::
	class Clown:
		name = "Trisha Perthen Ferdletate Torhalimil Ludwig Sonyetta Paghetti Careyeep"
		funniness = 1
		makeup = "a lot"
		
		
		def laugh (self) :
			if self.makeup == "a lot":
				print ("BWAH-HA-HA-HA-HA-HA-HA! I'M GOING TO MAKE YOU WISH YOU NEVER CAME TO THIS CARNIVAL! BWAAAHHH-HAAA-HAAAAAA!!")
			elif self.makeup == "only a little":
				print ("HAHA! WHAT will I have to do to make THIS little kid CRYYYY?")
			else:
				print ("I still have to think about how to torture this little kid in their beauty sleep. MWAH-HA-HA-HA!")
				
		def smile (self) :
			if self.funniness == 1:
				print ("YOU ARE LUCKY! TODAY I ONLY HAVE A FEEBLE SMILE WATTAGE. :)")
			elif self.funniness == 5:
				print ("HA HA HA! YOU ARE NOT IN LUCK! MY SMILE IS CHARGED FULLY! GOOD LUCK LIVING FOR ABOUT 2 MINUTES!")
			else:
				print ("MY AWESOMELY AWESOME NICENESS IS COMING INTO PLAY, BECAUSE I WILL GIVE Y0U 3 SECONDS TO RUN AWAY. GOOD LUUCCCKKK!")

				
The ``Tornado`` class:
::
	class Tornado:
		rank=0
		speed=72
		duration= 1

		def set_rank(self, rank_num):
			self.rank = rank_num
			if self.rank==0:
				self.speed=72
			elif self.rank==1:
				self.speed=112
			elif self.rank==2:
				self.speed=157
			elif self.rank==3:
				self.speed=205
			elif self.rank==4:
				self.speed=260
			elif self.rank==5:
				self.speed=318
			else:
				print('You screwed up! If you KNEW about tornadoes, you\'d KNOW that they go from 0 to 5')
				quit()

		def shout(self):
			# if self.rank==0:
			print("The tornado has rank " + str(self.rank), "we are going to see speeds up to " + str(self.speed))

			
The ``Computer_Virus`` class:
::
	class Computer_Virus:
		type = "Type A"
		power = 900000
		destruction_level = 900000000

		def destruction(self):

			if self.destruction_level == 1000000:
				print("erasing everything but your hairline because you don't have one")
			elif self.destruction_level == 900000000:
				print("..........................................................." * 723)
			else:
				print("jkasergtervfasdgfhygawebvfrn dsavgsvfheawhfaehdnhZbn,vfabndvfyukwevgbafj,evhfasdvkeujkvfhamdbmhvfasghdvqefhamehjvf" * 100)
				

The ``Door`` class:
::
	class Door:
		color = "brown"
		height = 7
		number = 5

		def a(self):
			if self.height == "7":
				print("good")
			if self.height >= "7":
				print("go away")
			if self.height <= "7":
				print("get out")



Homework
--------

Because we have 2 weeks until next class, try to do this assignment before next Sunday. Then on Sunday, I'll post another assignment for the following week.

For homework this week, you'll be writing another class. You can pick any object you want to write a class for - however, you need to include the following requirements:

1. The class should have at least 3 properties (remember, properties are just internal variables)
2. The properties should include at least one Boolean, at least one String, and at least one Int
3. The class should have at least 2 internal functions
4. At least 1 internal function needs to somehow use a property of the class (remember to use the ``self`` keyword!)
5. At least 1 internal function needs to return a value
6. At least 1 internal function needs to take an input argument
6. The functions and properties should be meaningfully named (for example, no names like "x," "a," or "var")

Then, once you've defined the class, write some code that does the following:

1. Make an object of that class
2. Change one or two of the properties of the class, so they aren't just the default values
3. Call the class's functions

This is mostly just a review of what we covered this week and last week. Next Sunday, the assignment will be a little more complex. 

Remember to send me an email at tmeo@njgifted.org if you have any questions. Good luck!!

Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1bxPpZBtE3FhP1WW_vLRvRaCaI3jUfbWL05ZhDyczNSw/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
