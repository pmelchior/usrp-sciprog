Exercises in somewhat arbitrary order:

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
