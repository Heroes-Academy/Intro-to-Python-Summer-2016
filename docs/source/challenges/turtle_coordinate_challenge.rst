.. A turtle challenge for a student
.. author: brian mcmahan
.. date: 2/4/2016


Turtle Challenge: Specific Coordinates
======================================

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
^^^^^^^^^^^^^

Use a coordinate list like the one above to make your initials (first and last).


