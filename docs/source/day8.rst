Day 8: Advanced Classes
========================


Take home work
--------------

You should work on your project.

Specialized tutorials
---------------------

1. :doc:`tutorials/turtle_artist.rst`
2. :doc:`tutorials/chatbot.rst`
3. :doc:`tutorials/minecraft_architect.rst`
4. :doc:`tutorials/data_analysis`

Review
-------

Two topics:

- The ``__init__`` function in classes
- Default arguments in functions


``def __init__(self)``
**********************

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

Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1Lgyi2knArQJXo9-7dEjvl7Un_UMcDHLtRRnWHV8F1QM/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
