Data Analysis Tutorial
======================


More datasets
-------------

1. `Simpler Datasets <https://vincentarelbundock.github.io/Rdatasets/datasets.html>`_
2. `A huge list of datasets <https://github.com/caesar0301/awesome-public-datasets>`_
3. `538's datasets <https://github.com/fivethirtyeight/data>`_

Overview
--------

The goal of this tutorial is to talk about the important parts of beginning data analysis.

The typical analysis pipeline goes through the following stages:

1. Think about the data you would like
2. Either find a way to collect that data, or find data that already exists
    - sometimes you might have to compromise on data because it's easier to just use stuff that exists already
3. Write code that takes the data from a file or database and loads it into a data structure
    - For python, this could mean loading it into a list or a dict
    - We might get to a more advanced data structure solution---Pandas---but we will cover the basics first.
4. Write code that puts the data into different forms that match the task you want to do.
    - For instance, if you want to view interesting properties of your data as a scatter plot, you need to get two lists: one for the x positions and 1 for the y positions


I will be writing this tutorial while looking at the titanic dataset. 
The titanic dataset is a list of passengers, information about them, and whether they survived or not.


Getting the Data
----------------

I have made the data easy to get:
::
    from urllib import request
    import pandas as pd
    filepath = 'https://gist.githubusercontent.com/braingineer/5d15057ac482ee0130b6d0e6f9cc9311/raw/d4eefaecc98b342ec578cf3512184556e8856750/titanic.csv'
    response = request.urlopen(filepath)
    df = pd.read_csv(response)
    df = df.fillna(0)


Using Pandas
------------

I will put more here soon, but here are some initial tutorials:

1. `Simple Graphics <http://pbpython.com/simple-graphing-pandas.html>`_
2. `Beautiful Plots <https://datasciencelab.wordpress.com/2013/12/21/beautiful-plots-with-pandas-and-matplotlib/>`_

Some simple operations:
::
    # select an entire column
    age_column = df['Age']
    
    # select a subset 
    df2 = df[age_column > 0]
    
    # view the columns
    print(df2.columns)

    # visualize a scatter plot
    plt.scatter(df2['Survived'], df2['Age']);
    # or with columns out
    surv_col = df2['Survived']
    age_col = df2['Age']
    
I will put up more later tonight. 




Old versions below
==================

I have changed the page to reflect the use of pandas. the old stuff is below. 



Getting the Data
----------------


I have made the data easy to get:
::
    from urllib import request
    filepath = 'https://gist.githubusercontent.com/braingineer/5d15057ac482ee0130b6d0e6f9cc9311/raw/d4eefaecc98b342ec578cf3512184556e8856750/titanic.csv'
    response = request.urlopen(filepath)
    data = response.readlines()
    
The data that is input here is a list of rows for the dataset.  Try and print out a couple.


Cleaning the Data
-----------------

Take this raw data and turn it into a cleaner version. 

To do this, you have to go through each line, replace the newline character with 
the empty string (so it is removed), and split on the comma.  

Since the first line is the headers, you know the name of each column. 

So, you can take this information and make a dictionary per line which uses the 
column names in the header as the keys and the values of each row as the values.  
I have made a function which does this for one line.  You have to figure out how to 
get the headers into a cleaned list, and how to apply this to every line in the file. 

This should involve:

1. to make the headers, replacing and splitting the first line in the data (``data[0]``) 
2. then, use a for loop over the rest of the data (``data[1:]``) an apply the function
    - You will need another list to save things to (``clean_data.append(...)`` where ``...`` is a place holder for code you should write)
example:
::
    def clean_one_line(line, headers):
        line = line.replace("\n", "")
        line = line.split(",")
        ### this is a fancy line.  play around with zip on your own. 
        ### zip lets you take two lists and make them into a list with them paired
        ### just like a zipper =)
        temp_dict = dict(zip(headers, line))
        should_be_ints = ['PassengerId']
        should_be_floats = []
        out_dict = dict()
        for key, value in temp_dict.items():
            if key in should_be_ints:
                out_dict[key] = int(value)
            elif key in should_be_floats:
                out_dict[key] = float(value)
            else:
                out_dict[key] = value
        return out_dict

Viewing the Data
----------------

Now that you have data in a list of dictionaries, you can view it!
Matplotlib is the python plotting library. You can import it like:
::
    import matplotlib.pyplot as plt
    
If you are using Jupyter notebook (which I highly recommend), you should also type this in:
::
    %matplotlib inline

If you are in the terminal, you should do the following. If you don't, every plot will take over the terminal and not let you type.
::
    plt.ion()

If you are running a file, you should do the following after every plot. 
::
    plt.show()

The reason it's shortcutted like this is because the alternative is too long. 
It's called ``plt`` because it's just what everyone does (and it's good to use a common convention)

There are a couple easy plots you can do:
::
    plt.plot
    plt.hist
    plt.scatter

You can see some basics at `this pyplot tutorial <http://matplotlib.org/users/pyplot_tutorial.html>`_.
But, you need to get your data into a certain form for this. 
Let's take the ``plt.hist`` for example.  This requires you to have a single list of numbers.
To do this, we now just iterate over our cleaned data:
::
    age_view = []
    for datum in cleaned_data:
        age_view.append(datum['Age'])
    plt.hist(age_view)
    
    