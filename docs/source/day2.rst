Day 2: Strings and Input
=========================


Summary
-------

We made it through a lot of material today. We started with a refresher on string operations
by doing the pig latin exercise. However, this exercise turned into a bunch of extra steps because you all were doing so awesome!

The extra steps were:
1. use ``input`` to get a word from the console
2. use a for loop and ``words.split(" ")`` to loop over words in a sentence and do pig latin to each.
:: 
    word = input("give me a word for piglatin: ")
    ### do your pig latin stuff here
    sentence = input("give me a sentence for piglatin: ")
    print("Split sentence: {}".format(sentence.split(" ")))
    for word in sentence.split(" "):
        ## do your pig latin stuff here
        print(word)

After we finished up that exercise, we worked through the shortcut math operations. 
Then, we talked about formatting strings.  You saw the curly bracket (``{}``) easy way. 
You should check the review out below. 

We rushed through some of the input and type conversion stuff. So, you should definitely try inputting numbers and then converting them for a math equation. 


In-Class and Homework Exercises
-------------------------------


I have updated the homeworks below to include some of our discussion at the end of class. 

All of the code is on the `Github Repository  <https://github.com/Heroes-Academy/Intro-to-Python-Summer-2016>`_. 

1. Go through ``formulas.py`` and do those problems.
2. Read through ``harder_formulas.py``, ``string_practice.py``, and ``build_in_practice.py``
    - try to do these problems. If you can't, let me know and I'll go over them
3. Break the code in some way. 
    - You should be writing down the error, what it says, and why it happened.
    - You should also send me code by tomorrow with how you made the error 
4. Do something fun with turtles. `The one I created in class is here <https://trinket.io/python/c9c47d373c>`_.  
Or if you scroll to the bottom of the page, I've embedded it there. 

See below for more details.



Review
------

After this class, you should know or practice all of these topics:

-	Inserting a new line in a String
-	Concatenating (combining) Strings
-	Repeating a String
-	Indexing Strings
-	Slicing Strings
-   Formatting Strings
-	Math Shortcuts
-	Converting between types
-	User Input

Inserting a new line in a String
********************************
You can use \\n in the middle of a String to make a new line. For example, the String “Hello, \\n World!” will print like this:
::
    Hello,
    World!

You can also use \\t in the middle of a String to make an indent. “Hello, \\t World!” will print like this:
::
    Hello,     World!

Concatenating Strings
*********************
You can combine Strings using the + sign.

Example: 
::
    str1 = “Hello”
    str2 = “World!”
    str3 = str1 + str2
    print(str3)

This will print out “HelloWorld!”

Repeating a String
******************
You can repeat Strings using the * sign

Example: 
::
    str1 = “bogdan”
    str2 = str1 * 3
    print(str2)

This will print out “bogdanbogdanbogan”

Indexing Strings
****************
You can get one character from a String using square brackets, []. Inside the square brackets, put the index of the character you want to get. In a String, the first character starts at index 0, and goes up from there. 

For example: If str = “computer”, then:

- str[0] is “c”
- str[1] is “o”
- str[2] is “m”

...and so on. 

You can put -1 in the brackets to get the last letter of a String too.

- str[-1] is “r”
- str[-2] is “e”

etc. 

Remember, every character gets its own index – even numbers, symbols, and spaces!

Slicing Strings
***************
By getting a slice of a String, you can get multiple characters all at once. Use square brackets for this too. Inside the brackets, you first put the starting index, then a colon, and then the ending index. 

For example:
::
    str = “fantastic!”
    print(str[0:3])

This will give you “fan”. It starts at 0, and stops just before the character at position 3. So, you get the letters at positions 0, 1, and 2. 

Some more examples:

- str[1:4] is “ant”
- str[0:2] is “fa”
- str[3:7] is “tast”

...and so on. If you leave out the first number, the slice will start at the beginning of the String.

- For example: str[:5] is “fanta”

If you leave out the second number, the slice will go until the end of the String.

- For example: str[2:] is “ntastic!”

Formatting Strings
******************

Formatting strings is necessary if you want to be able to print variables to the shell.

There are a couple different ways of formatting strings.  I will cover all three here.

**1. With string concatenation**
::
    animal = "bunny"
    adjective = "evil"
    noun = "the ruler of the world"
    
    our_sentence = "The "+adjective+" "+animal+" wants to be "+noun"."
    
    print(our_sentence)
    
**2. With string formatting**
::
    animal = "bunny"
    adjective = "evil"
    noun = "the ruler of the world"
    
    our_sentence = "The {} {} wants to be {}.".format(adjective, animal, noun)
    
    print(our_sentence)
    
The second way is much preferred because you can have fine grained control over formatting options:
::
    a_number = 3432.34234324233462
    print("Not formatted well: {}".format(a_number))
    print("Formatted: {:0.3f}".format(a_nubmer))
    
    a_string = "euclid the bunny"
    print("without formatting options: {}".format(a_string))
    print("with formatting options to right align: {:>50}  [end]".format(a_string))
    print("with formatting options to center align: {:^50} [end]".format(a_string))

The stuff inside the curly brackets specifies the options.  The options start with a colon.  
Then, if it's a number, you can specify the number of decimal points to have.  You need the 'f' for the float.

For strings, '>' aligns to the right, '<' aligns to the left, and '^' aligns to the center. 
The number directly after that is how wide it should be. It will add spaces to adjust. 

Math shortcuts
**************
Let’s say you’re writing code and have a variable x = 5. What if you want to increase x by 10?
You could do this: 
::
    x = x + 10 

Python gives you a shortcut way to write this:
::
    x += 10


``x += 10`` is a way of telling Python, “just increase x by 10.” You can also do ``x -= 10`` to decrease x by 10.

You can use this shortcut with the following math signs:

- +=
- -=
- *=
- **=
- /=
- %=

Converting between types
************************
In Python, variables all have a type. If you do ``my_number = 5.1234``, then the variable ``my_number`` has type Float (because it’s a number with a decimal point). 

In Python, sometimes you can convert variables to be a different type. For example, remember that there are two kinds of numbers in Python: int (no decimal) and float (with a decimal). You can convert from one to the other:
::
    my_float = 5.1234
    other_number = int(my_float)
    print(other_number)

This will print out 5. When you convert a float to an int, Python simply chops off the decimal part.

Or:
::
    my_int = 10
    some_float = float(my_int)
    print(my_int)

This will print out 10.0 (Python just adds a decimal point when you convert an int to a float).

If you have a String that is just a number, for example, var1 = “100”, you can convert that to an int or float! 
::
    var2 = int(var1)
    var3 = float(var1)


One note of caution: if you have a String variable like ``my_string_variable = “50.3”``, you can’t directly convert it to an Int (because it has a decimal point). If you want it to be an Int, you’d have to first convert it to a Float, and then to an Int.

Finally, you can convert just about anything to a String. 
::
    my_num = 505.606
    some_text = str(my_num)
    print(some_text)

This will print out “505.606” – a String!

User Input
**********
The last thing we learned in Week 2 was how to get user input. This is where you ask the user to type in a value, and can use that value in your code! You do it with the input() function. Inside the parentheses, you put a String, which is the message that the user will see. 

Here’s a quick example. Type the following code into the Python shell:
::
    user_name = input(“Please type in your name: ”)

If you type that code in and press enter, it will display the message, “Please type in your name: ” and wait for a response. Type something in (any name will do) and press enter. Then type the following code:
::
    print(user_name)

It should print back out whatever you typed in! The name you typed is saved in the variable ``user_name``, so you can treat it like any normal String. 

Maybe you want to print out how many letters are in your name:
::
    name_length = len(user_name)
    print(name_length)

…and so on. 

Quick note: whenever you get user input, the computer assumes it’s a String. So in the example above, ``user_name`` is a String. Even if the user types in a number, you get it as a String first. You can convert it to a number using the int() or float() functions we learned.



Lecture Slides
--------------

.. raw:: html

    <iframe src="https://docs.google.com/presentation/d/1YkwERJfgs5kBbtj8cXGVik010NLEpBE7Cqio8LBIFnI/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>


Trinkets
--------

.. raw:: html

    <iframe src="https://trinket.io/embed/python/c9c47d373c" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>