# Day 2: Introduction to python

## Location

CSML Auditorium, 26 Prospect Ave.

## Schedule

* 9:30 - 10:30 Introduction to python
* 10:30 - 11:00 Break
* 11:00 - 12:30 Python exercises
* 12:30 - 14:00 Lunch
* 14:00 - 15:30 Introduction to numpy
* 15:30 - 16:00 Break
* 16:00 - 17:00 Numpy exercises

## Command line and scripts

* Python in command line:

    ```
    remy$ python
    Python 3.7.1 (default, Dec 14 2018, 13:28:58) 
    [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('Hello campers!')
    Hello campers!
    >>> 
    ```

* Scripts:
Python commands in a file (see file `hello.py`)

    ```
    $ python hello.py
    Hello campers 
     how are you today?
    this is a script, which, when called, will execute all the line in it:
    for instance, I can declare functions and execute them. 
     Here I add 3 and -10 to make -7
    ```

* Script with arguments:
A file can be executed with arguments that are used in the script:

    ```
    $ python arguments.py 24 remy
    The following arguments were provided: 24
    Please give the description of input 0 with value 24
    age
    input number 0, with value 24 is a age
    Please give the description of input 1 with value remy
    name
    input number 1, with value remy is a name
    ```

* Python terminal:
It is possible to execute a script directly from the python terminal where other commands can be passed. 

    ```
    $ python
    Python 3.7.1 (default, Dec 14 2018, 13:28:58) 
    [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import hello
    Hello campers 
    how are you today?
    this is a script, which, when called, will execute all the line in it:
    for instance, I can declare functions and execute them. 
    Here I add 3 and -10 to make -7
    ```
  

Inside the python terminal, once a script or module is imported, it is possible to call functions from this module. 
Example, here:


    >>> hello.add_numbers(2,3)
    5


* Jupyter notebook: 
An interactive terminal to execute python commands and comment code with a nice presentation

    ```
    $ cd your_path_to/usrp_sciprog/day2/
    $ jupyter notebook
    ```
  

## Imports
Imports are a very convenient way to call functions from other files or packages, such that one file does not have to 
hold all the function in a given script or project.
A .py file can be imported in various different ways. Here I will showcase imports and the usage of functions contained 
in the imported file:

* full name import:
  
    ```
    >>> import hello
    >>> #usage:
    >>> hello.add_numbers(2,3)
    ```

* alias import for long or complex files or packages:

    ```
    >>> import hello as hi
    >>> #usage
    >>> hi.add_numbers(2,3)
    ```

* full content import:
I would generally advise against this course of action as it opens the way for multiple imports to contain functions or 
variables with identical names, thus making the usage of these functions confusing.

    ```
    >>> from hello import *
    >>> #usage
    >>> add_numbers(2,3)
    ```

* Specific import of a function or package content (with a little twick)

    ```
    >>> from hello import add_numbers as addn
    >>> #usage
    >>> addn(2,3)
    ```

## Practice

Now let's open "python-intro.ipynb"  and play with python's features. The following sections are all illustrated in this 
notebook.

### Variables:
In python, variables do not have to be declared before being attributed a value. For instance, `a = 3.` is all the 
variable declaration we need for a float variable.
In the notebook, we declare variables of different types: `int`, `float`, `str`, `list`. Many others exist and can be 
created (mystery).

### Operators:
The usual operators exist in python and have a simple form:
* Arithmetic operators:
    +    addition
    -    subtraction
    *    multiplication
    /    division
    //   floor division
    %    remainder of floor division
    **   power
    
* Relational operators:
    >    larger than
    >=   larger than or equal
    <    smaller than
    <=   smaller than or equal
    ==   equal
    !=   different
    
* Logical operators
    and
    or
    not
    in
    not in
    is 
    is not
    

A more in depth description of these operators can be fount here:
[https://data-flair.training/blogs/python-operator/](https://data-flair.training/blogs/python-operator/)

### Built-in functions
Python has a few default functions that facilitate implementation of  complex code. A full list of these functions can
 be found here:
[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html)
We highlight a few of them here and in the notebook:

    print('str')            prints a string
    len(array)              returns the length of an array
    max(array), min(array)  respectively returns the max and min values in an array
    sum(array)              sums the elements of an array
    type(x)                 returns the type of a variable
    str(x)                  makes a variable a string
    float(x)                makes a variable a float
    int(x)                  makes a variable an int
    range(n)                returns an array of integer numbers from 0 to n-1 
    enumerate(array)        returns the elements of an array along with their indexes

More functions can be created as we have seen previously.  To fully understand how to create functions, we need to 
understand a couple of simple, but nonetheless core features in python: Indenting and compound statements.

## Compound statements and indent:
Compound statements allow to execute groups of commands either repeatedly (for and while loops),  conditionally 
(if statements) or on demand (functions), among others. Each of these compound statements has a specific syntax, that 
relies on indentation of instructions.

Groups of instruction in a compound statement have to be indented. All instructions at the same level of indent are 
executed as a group. Ending an indent ends the group end hence the compound statement.

### Functions
A function has a simple structure. It is declared using the cammand `def`. A function has a `name`, some `arguments` and
 returns a `result`:

   
    def name(arguments):
        ''' short description
        longer description
        parameters
        arguments: type
            Description of argument
        returns
        result: type
            description of the result
        '''
        some_commands(arguments)
        return result
  

### For loops
For loops allow to perform repetitive operations on consecutive elements of an array. A `for` loop therefore needs an 
`array` and a name for an `iterator` inside the array:


    for iterator in array:
        operations_inside_loop
    other_operations_outside_loop


### While loops
While loops allow to perform repetitive operations as long as a condition is not met. A `while` loop needs an `condition` 
that should update at each iteration:


    while condition:
        operations_change_condition
    operations_once_condition_met

### If statements
If statement allow to execute a group of commands only if a condition is met. Several conditions can be put together to 
cover many cases. For that purpose, the elif statement is the logic equivalent to `else if`. Meaning that if the 
condition for the `if` is not met, the condition for `elif` should be tested and so on. the `else` statement covers all 
the cases not covered by `if` and `elif`s

 
    if condition1:
        operation
    elif condition2:
        operation2
    elif condition3:
        operation3
    else:
        operation4
    other_operations


## Commenting
Comments are lines not executed by python, that help you and and your collaborators to read a code and to make coding 
easier. Comments are declared by a `#` symbol. I HIGLY RECOMMEND using comments as much as possible! To add comments for
 code documentations, it is also possible to use ```'''... '''```.

# Introduction to numpy

Numpy is a package that allows to do maths with large arrays. 
Numpy is classically imported using the command:

    import numpy as np

I strongly advocate for the use of this syntax. Any other syntax will make potential collaborators hate you with 
all the fibers of their being. 

## ndarray
A core feature of this package is the `ndarray` which is the type that array declared using numpy take. 
There are many ways to declare array in numpy:


    np.ndarray(4)           an empty array of 4 elements
    np.zeros((3,4))         a 3 by 4 array of zeros
    np.ones((3,5,3))        a 3 by 5 by 3 array of ones
    np.arange(1,10,2)       an array of floats between 1 and 10 spaced by 2
    np.random.randn(4)      an array of 4 values drawn at random from a normal distribution

## Methods of ndarrays
Ndarrays have a set of methods, i.e. functions that can be called directly on the array using the syntax
`array.method(optional_arguments)`. These methods are inherited from numpy. As such, they can be calles as functions
 from numpy and write `np.method(array, optional_arguments)`. Among the most useful methods, we find:
    
    a.sum()             Sums all the elements in an array
    a.mean()            Computes the mean of its elements
    a.std()             Computes the standard deviation of its elements
    a.min(), a.max()    Computes the min and max of its elements
    a.sort()            Sorts the elements of an array
    a.dot(b)            Computes the dot (matrix) product of a and b
    a.reshape(newshape) reshapes into an array with the same number of elements
    a.flatten()         renders a multi-dimensional array as a line


For the rest, practice is better than words, let us take a look at a few examples.

# A quick word on IDEs

So far we have been using `emacs` or `vim` with command lines. 
There are other interpreters out there that have some nice features to make coding simpler and more comfy. 
Here are a few examples. You might now others. I invite you to look them up on line.

* VSCode
* Sublime
* idle
* atom (customizable)
* PyCharm (for python)
* Canpoy
