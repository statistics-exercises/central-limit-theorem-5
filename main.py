import matplotlib.pyplot as plt
import numpy as np

n = 20     # This is the number of bins in your histogram
counts = np.zeros(n) 
xmin, xmax = -4, 4  # This is the extent of the histogram it goes from xmin to xmax
delr = (xmax - xmin) / n  # this is the widths of the bins in the histogram
# Here you need a loop to generate 500 normal random variables with expectation 0 and variance 1.  You should use the list called counts to count how many of these random variables fall
# in each of the 20 bins that we divide the line segment between -4 and 4 into.



# Don't forget to normalise your distribution once you have completed
# sampling the random variable.


 
# I have written a loop for you here to generate the x values for the data 
# points and to plot the true pdf.
xdata, pdfvals = n*[0], n*[0]
for i in range(n) :
  xdata[i] = xmin + (i+0.5)*delr
  pdfvals[i] = ( 1 / np.sqrt(2*np.pi) )*np.exp( -xdata[i]*xdata[i] / 2 )

plt.plot( xdata, pdfvals, 'r-')
plt.plot( xdata, counts, 'ko' )
plt.savefig("mypdf.png")
