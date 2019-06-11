Schedule:

* 9:30 - 10:30 Introduction to python (+notebooks)  
* 10:30 - 11:00 AstroCoffee
* 11:00 - 12:30 Introduction to numpy + broadcasting exercise 
* 12:30 - 14:00 Lunch
* 14:00 - 14:30 Discussion (quick word on IDEs: text, IDLE, atom, pycharm…) 
* 14:30 - 15:00 Break
* 15:00 - 17:00 Estimate pi (+ more exercises around object oriented programming if time permits)

# Introduction to python:

## Command line and scripts

* Python in command line:

    '''
    remy$ python
    Python 3.7.1 (default, Dec 14 2018, 13:28:58) 
    [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('Hello minions!')
    Hello minions!
    >>> 
    '''

* Scripts:
Python commands in a file (see file `hello.py`)

    '''
    remy$ python hello.py
    Hello minions 
     how are you today?
    this is a script, which, when called, will execute all the line in it:
    for instance, I can declare functions and execute them. 
     Here I add 3 and -10 to make -7
    '''

* Script with arguments:
A file can be executed with arguments that are used in the script:

    '''
    remy$ python arguments.py 24 remy
    The following arguments were provided: 24
    Please give the description of input 0 with value 24
    age
    input number 0, with value 24 is a age
    Please give the description of input 1 with value remy
    name
    input number 1, with value remy is a name
    '''

* Python terminal:
It is possible to execute a script directly from the python terminal where other commands can be passed. 

    '''
    remy$ python
    Python 3.7.1 (default, Dec 14 2018, 13:28:58) 
    [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import hello
    Hello minions 
    how are you today?
    this is a script, which, when called, will execute all the line in it:
    for instance, I can declare functions and execute them. 
    Here I add 3 and -10 to make -7
    '''

Inside the python terminal, once a script or module is imported, it is possible to call functions from this module. Example, here:


    >>> hello.add_numbers(2,3)
    5

* Jupyter notebook: 
An interactive terminal to execute python commands and comment code with a nice presentation


    remy$ cd your_path_to/usrp_sciprog/day2/
    remy$ jupyter notebook

  

## Imports
Imports are a very convenient way to call functions from other files or packages, such that one file does not have to hold all the function in a given script or project.
A .py file can be imported in various different ways. Here I will showcase imports and the usage of functions contained in the imported file:

* full name import:

    >>> import hello
    >>> #usage:
    >>> hello.add_numbers(2,3)

* alias import for long or complex files or packages:

    >>> import hello as hi
    >>> #usage
    >>> hi.add_numbers(2,3)

* full content import:
I would generally advise against this course of action as it opens the way for multiple imports to contain functions or variables with identical names, thus making the usage of these functions confusing.
markdown

    >>> from hello import *
    >>> #usage
    >>> add_numbers(2,3)

* Specific import of a function or package content (with a little twick)


    >>> from hello import add_numbers as addn
    >>> #usage
    >>> addn(2,3)

# Practice

Now let's open "python-intro.ipynb"  and play with python's features. The following sections are all illustrated in this notebook.

##Variables:
In python, variables do not have to be declared before being attributed a value. For instance, `a = 3.` is all the variable declaration we need for a float variable.
In the notebook, we declare variables of different types: `int`, `float`, `str`, `list`. Many others exist and can be created (mystery).

## Operators:
The usual operators exist in python and have a simple form:
### Arithmetic operators:
    +    addition
    -    subtraction
    *    multiplication
    /    division
    //    floor division
    % remainder of floor division
    ** power
### Relational operators:
    >    larger than
    >=  larger than or equal
    <    smaller than
    <= smaller than or equal
    == equal
    !=  different
### Logical operators
    and
    or
    not
    in
    not in
    is 
    is not
A more in depth description of these operators can be fount here:
[](https://data-flair.training/blogs/python-operator/)

## Built-in functions
Python has a few default functions that facilitate implementation of  complex code. A full list of these functions can be found here:
[](https://docs.python.org/3/library/functions.html)
We highlight a few of them here and in the notebook:
print('str') prints a string
len(array) returns the length of an array
max(array), min(array) respectively returns the max and min values in an array
sum(array) sums the elements of an array
type(x) returns the type of a variable
str(x) makes a variable a string
float(x) makes a variable a float
int(x) makes a variable an int
range(n) returns an array of integer numbers from 0 to n-1 
enumerate(array) returns the elements of an array along with their indexes

More functions can be created as we have seen previously.  To fully understand how to create functions, we need to understand a couple of simple, but  nonetheless core features in python: Indenting and compound statements.

Compound statements and indent:
    compound statements allow to execute groups of commands either repeatedly (for and while loops),  conditionally (if statements) or on demand (functions), among others. Each of these compound statements has a specific syntax, that relies on indentation of instructions.
Groups of instruction in a compound statement have to be indented. All instructions at the same level of indent are executed as a group. Ending an indent ends the group end hence the compound statement.
    Let's see how this works by declaring a function that


markdown

- Commenting
    Comments are lines not executed by python, that help you and and your collaborators to read a code and make coding easier. Comments are declared by a '#' symbol. I HIGLY RECOMMEND using comments as much as possible! To add comments for code documentations, it is also possible to use '''... '''.
- Compound statements:
    if ... elif ... else
All Comments
ActiveResolved
No comments to display
