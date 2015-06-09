Day 1 Exercises
===============

Do each of the following exercises, submitting the solutions via pull requests to this repository (see the git-intro notes).

**RULES**

* Every variable/function/class name should be meaningful
* Variable/function names should be lowercase, class names uppercase
* Write a documentation string (even if minimal) for every function.

1) Create a file called ``hello.py`` that can be used in both of the following ways:

* From the system command line::

    $ ./hello.py
    Hello world!

* From the python command line::

   >>> import hello
   >>> hello.hello()
   Hello world!

2) (From `@jakevdp <https://github.com/jakevdp/2014_fall_ASTR599/blob/master/notebooks/01_basic_training.ipynb>`_): Create a program (a .py file) which repeatedly asks the user for a word. The program should append all the words together. When the user types a "!", "?", or a ".", the program should print the resulting sentence and exit.

   For example, a session might look like this::

    $ ./make_sentence.py
    Enter a word (. ! or ? to end): My
    Enter a word (. ! or ? to end): name
    Enter a word (. ! or ? to end): is
    Enter a word (. ! or ? to end): Walter
    Enter a word (. ! or ? to end): White
    Enter a word (. ! or ? to end): !
    
    My name is Walter White!
    

3) (From `@jakevdp <https://github.com/jakevdp/2014_fall_ASTR599/blob/master/notebooks/01_basic_training.ipynb>`_):  Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”. If you finish quickly... see how **few** characters you can write this program in (this is known as "code golf": going for the fewest key strokes).

4) Write a function called ``sum_digits`` that returns the sum of the digits of an integer argument; that is, ``sum_digits(123)`` should return ``6``.  Use this function in a program called ``sum_digits.py`` that prints out the sum of the digits of every integer multiple of the first argument, up to either the second argument (if included) or the first argument's square.  That is::

    $ ./sum_digits.py 4
    4
    8
    3
    7
    $ ./sum_digits.py 4 20
    4
    8
    3
    7
    2


5) Write a program called ``wordfreq.py`` that prints out all words longer than three letters (and their frequencies) in a given file, ordered by frequency.  Run this on ``ihaveadream.txt``, and check it vis-a-vis ``ihaveadream_freqs.txt``, which has my results of this exercise::

    $ head ihaveadream_freqs.txt
    will: 27
    that: 24
    this: 20
    freedom: 20
    from: 18
    have: 17
    with: 16
    negro: 13
    ring: 12
    dream: 11

6) Some fun with object-oriented programming: make a file called ``solarsystem.py`` that defines ``Star``, ``Planet``, and ``System`` objects that enable the provided notebook file to work as demonstrated.  If you finish this, feel free to add more functionality to these objects!

    
