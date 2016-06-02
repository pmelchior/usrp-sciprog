#Fit a transiting planet signal with a trapezoid model


1.  Write a function that takes a filename as an argument and returns two
arrays: `time` and `flux`, read from the file.

2.  Write a function that takes a filename as an argument and plots time vs.
flux.  

3.  Write a function implementing the trapezoid model.  It should take four
parameters (`delta, T, tau, t0`---depth, duration, ingress duration, and
    center time) and return a trapezoid as a function of time.  

4.  Write a function that will take an Nx4 array of trapezoidal parameters
and plot a different trapezoid for each row of parameters (all at the same
   time values).

5.  Use (4) to make four different plots that show how the trapezoid shape
changes when you vary each parameter independently (maybe 10 examples per
    plot).

6.  Eyeball the plot of the actual 7016.01 transit signal, and try to guess
what parameters might fit the data best.  Overplot the model on top of the
data, and make a plot of the residuals (data - model) in a subplot.  Your
first guess doesn't have to be spot-on---the residuals should tell you where
you're off the most.

7.  Use what you did in (6) to write a function that takes a filename and a
parameter vector, and then makes the data + models + residuals plot.

8.  Use `scipy.optimize` to find the best-fit parameters for the 7016.01
data set, and display these results using (7).

9.  Re-structure the above code using a custom-defined `TransitSignal`
object so that you can do the following:

        signal = TransitSignal(7016.01) 
        signal.plot()  # This plots only the data
        signal.plot(params=[0.0005, 15, 3, 0.])  # this: model/data/residuals
        best_params = signal.best_fit()
        signal.plot(params=best_params)

If you get to the point where you can do (9), you are set up to automatically
analyze thousands of signals with just a few lines of code!

