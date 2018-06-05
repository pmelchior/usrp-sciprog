Day 2 Exercises: Basic numpy & matplotlib
--------

1. Create the following arrays:

    ```
    [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 2],
     [1, 6, 1, 1]]

    [[1., 0., 0., 0., 0.],
     [0., 2., 0., 0., 0.],
     [0., 0., 3., 0., 0.],
     [0., 0., 0., 4., 0.],
     [0., 0., 0., 0., 5.]]
    ```

2. Create a two-dimensional array with shape (16, 64) fill all 64 columns
   identically with the Fibonacci sequence (16 values from the sequence). Select
   the sub-array that contains all even numbers from this array.

3. Generate an array of random numbers sampled from a Uniform distribution
   between 2 and 16, then change the data type of the array to integer. Using a
   boolean index array, select all even values from this array between 5 and 10.

4. Write a function to evaluate a 2D Gaussian function. The function should
   accept: two arrays (an array of `x` values and an array of `y` values), a
   length-2 vector of the means along each dimnsion, and a 2D covariance matrix.
   It should return an array with the same shape as the input x or y array. The
   Gaussian function is:

   ![Gaussian](gaussian.png)


   for mean vector $\vec{\mu}$ and covariance matrix $\Sigma$.

   This code should work with your function:

   ```python

    import matplotlib.pyplot as plt

    x = np.arange(0.,10.,0.1)
    y = np.arange(0.,10.,0.1)
    x,y = np.meshgrid(x,y)
    mean_xy = np.array([5.,4.])
    cov = np.array([[1.,1.],
                    [1.,2.]])**2.

    f = gaussian2D(x.ravel(), y.ravel(), mean_xy, cov)
    f.reshape(100,100)

    plt.imshow(f.reshape(100,100))
    ```

5. Write a program that estimates the value of pi by the 'throw darts at a wall'
   method.  That is, generate random `(x,y)` points and see if they fall within
   the unit circle, and use these results to estimate pi.  For this exercise,
   make a module called `pi_estimate` within a `day2/exercises/yourname` folder.
   Make this module not as a single `.py` file, but rather as a folder called
   `pi_estimate` with a `__init__.py` file inside.  Besides these instructions,
   I will not give any more requirements to how you structure this exercise.
   You may want to start with just writing functions and then at some point
   reorganize into an object-oriented design.

	* Do this estimate using 100, 1000, 10,000, and 1e6 points.
    * How long does the calculation take for different numbers of points?  Make
      a figure that illustrates how the calculation time depends on the number
      of points.
	* Make a figure that displays the "darts."
    * Run this calculation many times for a single `N` (number of darts), and
      plot a histogram of the results.  What is the mean and standard deviation
      of these estimates?
    * Make a plot that illustrates the precision of the pi estimate as a
      function of number of random points used.

    Make a notebook that demonstrates how your `pi_estimate` module works, as
    well as presenting the results of all your calculations.  The notebook
    should have minimal complicated code in it; rather, it should initialize
    objects and call functions defined within the `pi_estimate` module.
