Week 3: PyCharm, Booleans, and If Statements
===============

Summary
^^^^^^^

We started class with a review of Week 02's material. If you want to review again, you can either use the lecture slides, or look at the Week 02 summary.

We also talked about PyCharm, a program you can use to write code. PyCharm is different than using the IPython shell; in the shell, you type one line of code at a time, hit Enter, and see what happens. PyCharm lets you write as many lines of code as you want, and then have the program execute them all, one after another. This is super useful if you're writing a long or complicated program. It's also a big time-saver, since you can run the same code over and over again without having to re-type it each time!

PyCharm also lets you **save** Python files, which is useful if you start to write code in class, and maybe want to bring it home with you or work on another computer. You can save a Python file (it will end in .py) and e-mail it to yourself or copy it onto a USB drive.

To practice using PyCharm, we wrote a program that lets you type in a word and get the Pig Latin translation. If you want some extra practice with PyCharm, try writing this program yourself at home!

Next we talked about Booleans. Booleans are variables that can have a value of ``True`` or ``False``. You can set Boolean variables in code with something like ``x = True``, or you can use **comparison operators.** 

These are the comparison operators we discussed:

- < less than
- > greater than
- <= less than or equal to
- >= greater than or equal to
- == equal to (remember, in Python, "equal to" uses two equals signs, because one equals sign is just used for making a variable)
- != not equal to

Comparison operators compare the values of two different variables, and will evaluate to either True or False. For example, ``5 > 3`` will evaluate to ``True``, but ``10 == 9`` will evaluate to ``False``. You can use these to make Boolean variables as well.

Booleans can also be combined using the ``and`` and ``or`` keywords. If ``x`` and ``y`` are Booleans, the expression ``x and y`` will only be ``True`` if both ``x`` and ``y`` are ``True``. ``x or y`` will only be ``True`` if at least one of them is ``True``. And of course, ``not x`` will just be the opposite of ``x``.

We practiced evaluating Booleans using cards and complex conditions (suite == hearts and not number <= 5).

Finally, we introduced the If Statement. An If Statement is comprised of two ingredients: a condition (which must be a Boolean), and some code. Python checks if the condition is True; if it is, the code will be executed. But if the condition is False, Python will just ignore the code and move on.

If statements kind of resemble a paragraph - the condition goes at the top, and the accompanying code is all indented by 4 spaces.
::
	if <condition>:
		do some code
		do some more code
	back to normal code
	
The computer knows when the If Statement paragraph ends because the indentation stops. That's all!

We also took a sneak preview at the ``Turtles`` module, but that will be covered in next week's lesson.


In-Class and Homework Exercises
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I want to make sure everyone's PyCharm is working properly, since a few people mentioned they'd had some trouble. Now that we've used PyCharm in class, try using it at home, `following the guide on the Week 3 Github page <https://github.com/Heroes-Academy/Intro-to-Python-Spring-2016/tree/master/code/Week%2003>`_. The filename is "Using PyCharm.pdf", and you can either view it directly on GitHub, or download it.

Email me back once you've tried it out, and let me know either if it worked, or if you ran into a problem! If you had a problem, just describe what it was, maybe with a screenshot of the issue. We'll work to get it sorted out, and then proceed from there.

Good luck!


Extra Resources
^^^^^^^^^^^^^^^


Lecture Slides
^^^^^^^^^^^^^^

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/19ZBXLQZNIYVQDRpiXFxIKeccMw3QvHT4T0F89_NCFQo/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
