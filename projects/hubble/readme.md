# Calculate the expansion velocity of the universe

In 1929, Edwin Hubble published a paper in which he compared the radial velocity of objects with their distance. The former can be done pretty precisely with spectroscopy, the latter is much more uncertain. His original data are [here](table1.txt).

He saw that the velocity increases with distance and speculated that this could be the sign of a cosmological expansion. Let's find out what he did.

1. Load the data into an array with `numpy.genfromtxt`. You will find 6 columns

   * `CAT`, `NUMBER`:  These two combined give you the name of the galaxy.
   * `R`: distance in Mpc
   *  `V`: radial velocity in km/s
   *  `RA`, `DEC`: equatorial coordinates of the galaxy 

2. Make a scatter plot of `V` vs `R`. Don't forget labels and units...

3. Use `np.linalg.lstsq` to fit a linear regression function and determine the slope $H_0$ of the line $V=H_0 R$. For that, reshape `R` as a Nx1 matrix (the so-called [design matrix](https://en.wikipedia.org/wiki/Design_matrix)) and solve for 1 unknown parameter. Add the best-fit line to the plot. 
   Why is there scatter with respect to the best-fit curve? Is it fair to only fit for the slope and not also for the intercept? How would $H_0$ change if you include an intercept in the fit?

4. `V` is a combination of any assumed cosmic expansion and the motion of the sun with respect to that cosmic frame. Generalize the model to $V=H_0 R + X \cos(RA)\cos(DEC) + Y\sin(RA)\cos(DEC)+Z\sin(DEC)$ and construct a new Nx4 design matrix for the four unknown parameters $H_0, X, Y, Z$ to account for the solar motion. Use the functions in [coordinates.py](coordinates.py) to convert the coordinate strings `RA` and `DEC` to floating points coordinates in degrees. The resulting $H_0$ is Hubble's own version of the "Hubble constant". What do you get?

5. Make a scatter plot of `V-VS` vs `R` where `VS` is the solar velocity (from 4). Add the best-fit linear regression line.

6. Can you estimate the age of the universe from $H_0$? Does it make sense?

### Extra points: Deconstructing `lstsq`

So far we have not incorporated any measurement uncertainties. Can you guess or estimate them from the scatter with respect to the best-fit line? You may want to look at the residuals returned by `np.linalg.lstsq`...

If you adopt a suitable value $\sigma$ for those uncertainties, how would that affect the estimate of $H_0$?

The problem you solved so far is $Ax=b$, and errors don't occur. With errors the respective equation is changed to $A^\top \Sigma^{-1} Ax=A^\top \Sigma^{-1}b$, where in this case the covariance matrix $\Sigma=\sigma^2\mathbf{1}$. This problem can still be solved by `np.linalg.lstsq`.

1. Construct the modified design matrix and data vector and get a new estimate of $H_0$. Has it changed? Use `np.dot `, `np.transpose`, and `np.linalg.inv`.

2. Compute the parameter covariance matrix $S=(A^\top \Sigma^{-1} A)^{-1}$ and read off the variance of $H_0$. How large is the relative error?  Would that help with item 6) above?

3. Compare your result from 1) with $SA^\top \Sigma^{-1}b $.
