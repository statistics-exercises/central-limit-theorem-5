import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_xplot(self) : 
        fighand = plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) :
           self.assertTrue( xmin + np.fabs( (xmax-xmin)*(i+0.5)/len(this_x) - this_x[i] )<1e-7, "the x-coordinates in your histogram are not correct" )
    
    def test_normalised(self) : 
        ssum = 0.
        fighand = plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) : ssum = ssum + this_y[i]*(this_x[1]-this_x[0])
        self.assertTrue( np.fabs(ssum - 1.)<1e-7, "your histogram is not normalised" )
    
    def test_plot(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        delx = this_x[1] - this_x[0]
        for i in range( len(this_y) ) :
            pp = st.norm.cdf( this_x[i] + 0.5*delx ) - st.norm.cdf( this_x[i] - 0.5*delx )
            bar = np.sqrt( pp*(1-pp) )*st.norm.ppf( (0.99 + 1) / 2 )
            self.assertTrue( np.fabs( this_y[i]- st.norm.pdf( this_x[i] ) )<bar, "the y-coordinates in your histogram appear to be incorrect" )
    
