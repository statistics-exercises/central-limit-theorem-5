# Histogram for Normal Random Variable

Let's finish our Pythonic exploration of the normal distribution by estimating the probability density function for a normal random variable by computing a histogram.  To complete the code in the cell on the right you must:

1. Write a loop that generates 500 normal random variables that have expectation 0 and variance 1.
2. Use the list called `counts` to count how many of each of these random variables fall into each of the 20 bins that we have divided the line segment between -4 and +4 into.
3. Write a loop that normalises the histogram in `counts`.  By the time you exit this loop the integral of the pdf you have estimated over the whole x axis should be one.

At variance with the way that I have presented the histogram problems in previous exercises, I have calculated the x-coordinates at which to plot each of the y-values in counts for you.  My reason for doing this is that I have written code to draw the true pdf in the figure as well as the estimate that you get by sampling.  The true probability density function is shown as a red line while your estimate will be indicated using a series of black dots. 

N.B.
_For this example, I have used a rather small number of bins for the histogram because we are only generating 500 random variables, which is not enough statistics to converge the histogram with a larger number of bins.  We are only generating 500 random variables because the server that we are running the calculations on does not give us access to much computing power.  If you run similar calculations using a python notebook you can easily generate many more samples and get much better data._ 
