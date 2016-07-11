Week 8: Advanced Classes
========================


Summary
-------

This lesson was split up into two segments:

- First, we learned about the ``__init__`` function in classes
- Second, we spent most of the lesson reviewing everything we've learned so far about Python.


The ``__init__`` function is one of Python's special functions - this is indicated by the double underscore (__) on either side of the function name. ``init`` is a keyword (like ``print`` or ``if``) and Python already knows what it's used for.

When you write your own class, sometimes it's helpful to have a kind of setup function that runs whenever you make a new copy of the class. For example, if you write the ``Door`` class we've been using as an example, you might want the ``Door`` to print out "Hello!" the first time someone makes it. And, every new ``Door`` that gets made will also say "Hello!"

This is what the ``__init__`` function is for: it's a special function that runs once every time an object of that type (in our example, ``Door``) is made.

So, for example:
::
  class Door:
    def __init__(self):
      print("Hello!")
      
  first_door = Door()
  second_door = Door()
  
The code above will print out "Hello!" twice - once for ``first_door``, and again for ``second_door``.

That's an example of an ``__init__`` function that doesn't take any arguments. Usually, this isn't the case - because ``__init__`` is a setup function, you want the user to provide certain information about the object when they make it. 

Here's an example:
::
  class Door:
    def __init__(self, in_name, in_height):
      self.name = in_name
      self.height = in_height
      print("Hello! My name is " + self.name)
    
  first_door = Door("Gerald", 10)
  second_door = Door("Geraldina", 12)

In this code, when a ``Door`` object is created, it takes two arguments: the name, and the height. These arguments are then used for setting up the Door object (i.e., they set up the properties ``self.name`` and ``self.height``)

After that, we did a big review - all the questions and answers are included in the lecture slides, so you can use them if you want to brush up on old material. 


Homework
--------

No homework this week - just review what we've learned to prepare for your final project!

Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1NruISrIgHdI_w5oG5kOUCvsQkXm7gsUvGJnQVb3AcVs/embed?start=false&loop=false&delayms=30000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
