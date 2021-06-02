# Opt-out Challenge for Bootcamp

We know that you, as a student cohort, will have a wide spread of programming capabilities. What we intend to do with the bootcamp is to provide a background of scientific programming in a condensed form over 4 days. Some of you may know the relevant material already, though. If you can solve the following problem within 1 hour, you can ask to opt out from any or all parts of the bootcamp. **Do not worry if you cannot solve this problem, this is exactly what the bootcamp will teach you.**

## Problem

Assume that you have an experiment, where you control the x-variable, and you record the y-variable as well as its associated standard deviation. Your experiment yields this data set:

| x | y | y_std |
|---|---|--------|
| 0.5488 | 0.8243 | 0.0529 |
| 0.7152 | 1.1299 | 0.1548 |
| 0.6028 | 0.8912 | 0.0912 |
| 0.5449 | 0.7326 | 0.1137 |
| 0.4237 | 0.7115 | 0.0038 |
| 0.6459 | 1.0423 | 0.1235 |
| 0.4376 | 0.7381 | 0.1224 |
| 0.8918 | 1.2995 | 0.1234 |
| 0.9637 | 1.2154 | 0.1887 |
| 0.3834 | 0.6087 | 0.1364 |
| 0.7917 | 1.1072 | 0.0719 |
| 0.5289 | 0.8154 | 0.0874 |
| 0.5680 | 0.7820 | 0.1395 |
| 0.9256 | 1.2761 | 0.0120 |
| 0.0710 | 0.2337 | 0.1334 |
| 0.0871 | 0.1807 | 0.1341 |
| 0.0202 | 0.0630 | 0.0421 |
| 0.8326 | 1.2118 | 0.0258 |
| 0.7782 | 1.0834 | 0.0631 |
| 0.8700 | 1.2433 | 0.0727 |
| 0.9786 | 1.4330 | 0.1140 |
| 0.7992 | 1.1750 | 0.0877 |
| 0.4615 | 0.9862 | 0.1977 |
| 0.7805 | 1.1181 | 0.0204 |
| 0.1183 | 0.2984 | 0.0418 |
| 0.6399 | 0.9602 | 0.0323 |
| 0.1434 | 0.2053 | 0.1306 |
| 0.9447 | 1.2868 | 0.0507 |
| 0.5218 | 0.8090 | 0.0933 |
| 0.4147 | 0.7025 | 0.0489 |

1. Create a jupyter notebook.
2. Copy the data from here into a `numpy` array. (Or, you can read in the [data file](https://github.com/pmelchior/usrp-sciprog/blob/master/data.txt).) Make a plot of the data with `matplotlib`. 
3. Fit a quadratic model, i.e. determine the Maximum-Likelihood Estimator of the parameters `a,b,c` for a model of the form `y = a + b*x + c*x^2.` Note that the standard deviations of every y-value is different. 
4. Add the best-fitting line to your plot. Save the notebook.
5. Create a github repository. Upload/push your notebook. Create an issue [here](https://github.com/pmelchior/usrp-sciprog/issues), entitled "Bootcamp Opt-out", which contains the link to your github repo.

However, if you can solve this and want to help your fellow students, we can always use another mentor for the bootcamp. Let us know in your issue if you want to help.
