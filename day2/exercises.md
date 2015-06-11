Day 2 Exercises: Basic numpy & matplotlib
--------


1.  Write a program that estimates the value of pi by the 'throw darts at a wall' method.  That is, generate random `(x,y)` points and see if they fall within the unit circle, and use these results to estimate pi.  For this exercise, make a module called `pi_estimate` within a `day2/exercises/yourname` folder.  Make this module not as a single `.py` file, but rather as a folder called `pi_estimate` with a `__init__.py` file inside.  Besides these instructions, I will not give any more requirements to how you structure this exercise.  You may want to start with just writing functions and then at some point reorganize into an object-oriented design.

	* Do this estimate using 100, 1000, 10,000, and 1e6 points.
	* How long does the calculation take for different numbers of points?  Make a figure that illustrates how the calculation time depends on the number of points.
	* Make a figure that displays the "darts."
	* Run this calculation many times for a single `N` (number of darts), and plot a histogram of the results.  What is the mean and standard deviation of these estimates?
	* Make a plot that illustrates the precision of the pi estimate as a function of number of random points used.

	Make a notebook that demonstrates how your `pi_estimate` module works, as well as presenting the results of all your calculations.  The notebook should have minimal complicated code in it; rather, it should initialize objects and call functions defined within the `pi_estimate` module.   