Installing Minecraft
====================

README
------

The software used for this course is provided as companion to the book 
`Learn to Program with Minecraft <http://nostarchpress.com/pythonwithminecraft>`_.  
It is recommended that the students purchase the book.

To get things running, you will need:
 
 1. Minecraft
 2. Python 3
 3. Java
 4. Minecraft Python API
 5. The Minecraft server

Minecraft
^^^^^^^^^

Visit `the Minecraft homepage <http://www.minecraft.net>`_ to download.  If you do not
have an account, please email me and I will make sure you are provided with one. 


Python 3 Distribution
^^^^^^^^^^^^^^^^^^^^^

Python 3 is the distribution we will be using. 
If you have Python 2, it is recommended that you uninstall Python 2 and install Python 3.
If you don't, there will be some inconsitencies that could be devestatingly confusing. 
Also, Python 3 has a lot of really cool, new features that aren't in Python 2. 

There are several ways to get Python.  I personally recommend the 
`Anaconda <https://www.continuum.io/downloads>`_ distribution.
It has a bunch of things packaged with it above and beyond Python that make it useful.
Anaconda comes with the Spyder editor.  It is a decent editor, but I would recommend:

  - `PyCharm <https://www.jetbrains.com/pycharm/download/>`_.
    
    - If you download PyCharm, make sure you download the Community Edition.
  
  - `Sublime Text <https://sublimetext.com/>`_ 
    
    - This is my personal favorite.  It is lightweight and has many extensions. 
    - However, it does not run or debug Python files as easily as PyCharm.
  
  - `Atom <https://atom.io/>`_
  
    - Very similar to Sublime

Java
^^^^

You should have both Minecraft and Python installed at this point. 
You need to set Java up in order to run the server. 

If you are on Windows:

  1. Click the Start Menu (or press the Windows key)
  2. Type "cmd" to find the program called cmd. Open this.

    - This is the command prompt.  It is also called a terminal or console.

  3. Type **java -version** at the prompt
  4. If you see an output describing the version of Java, you already have it and can continue to the next section.
  5. If you don't, or it can't find java, then go to here: http://www.java.com/en/download/
  6. Click **Free Java Download**.  Then click **Agree** and **Start**
  7. When it is finished downloading, install this. 
  8. **IMPORTANT**: If it asks you to install extra things or set Yahoo! as your homepage, click no.

    - This is the annoying feature about installed Java.

  9. Retry steps 1-3.  If they succeed, move on. If they don't, email me.

Minecraft Python API and Minecraft Spigot server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An API is an *interface*.  We will use it as a library that lets us communicate 
with the Minecraft server.  We will not be able to edit the server in any way, but 
instead, just tell it instructions.  

We will be using the Spigot server because it allows for the API to talk to it. 
Standard Minecraft does not. 

To install both of these:

  1. Go to https://www.nostarch.com/pythonwithminecraft/
  2. Download the MinecraftTools.zip for your operating system. 
  3. When it has finished downloading, you can open it.

    - a zip file is known as a compressed file
    - it allows you to compress a set of files to make them smaller for downloading
    - all operating systems let you open these files
    
  4. **Important** Although it looks like you have a folder, the contents of the Zip file are not a folder
  5. Create a folder somewhere convenient and name it *MinecraftTools*.
  6. Inside the Zip file, you can click "Extract all" or similar button.
  7. Extract it to your *MinecraftTools* folder. 
  8. Go to the folder and double click the **Install_API** file. 
  9. Now, you can run the server.  
  10. There is a file called **Start_Server**.  Running this will start the server.
  11. If you have any trouble, email me. 