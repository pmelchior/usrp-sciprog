#Fit a transiting planet signal with a trapezoid model


1.  Write a function that takes the object numer (e.g. 7016.01) as an argument
and returns two arrays: `time` and `flux`, read from the data file ('data/7016.01.txt').  

2.  Write a function that takes the object number as an argument and plots time vs.
flux of the data returned by (1).  

3.  Write a function implementing the trapezoid model.  It should take four
parameters (`delta, T, tau, t0`---depth, duration, ingress duration, and
    center time) and return a trapezoid as a function of time.  

4.  Make four different plots that show how the trapezoid shape
changes when you vary each parameter independently (maybe 10 examples per
    plot).

5.  Eyeball the plot of the actual 7016.01 transit signal, and try to guess
what parameters might fit the data best.  Overplot the model on top of the
data, and make a plot of the residuals (data - model) in a subplot.  Your
first guess doesn't have to be spot-on---the residuals should tell you where
you're off the most.

6.  Use what you did in (5) to write a function that takes a filename and a
parameter vector, and then makes the data + models + residuals plot.

7.  Use [scipy.optimize.minimize](http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize) to find the best-fit parameters for the 7016.01
data set, and display these results using (6).

8.  [Extra Credit] Re-structure the above code using a custom-defined `TransitSignal`
object so that you can do the following:

        signal = TransitSignal(7016.01) 
        signal.plot()  # This plots only the data
        signal.plot(params=[0.0005, 15, 3, 0.])  # this should plot model+data+residuals
        best_params = signal.best_fit()
        signal.plot(params=best_params)

If you've done this successfully, you are set up to automatically
analyze thousands of signals with just a few lines of code!

