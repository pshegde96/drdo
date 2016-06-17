from pykalman import KalmanFilter
from pylab import *
#kf = KalmanFilter(transition_matrices = [[1, 1], [0, 1]], observation_matrices = [[0.1, 0.5], [-0.3, 0.0]])

kf = KalmanFilter()
#measurements = array([[1,0], [0,0], [0,1]])  # 3 observations

'''Generating Data'''
# script to generate data files for the least squares assignment
from pylab import *
import scipy.special as sp
N=101 # no of data points
k=1   # no of sets of data with varying noise
# generate the data points and add noise
t=linspace(0,10,N)     # t vector
y=1.05*sp.jn(2,t)-0.105*t # f(t) vector
Y=meshgrid(y,ones(k),indexing='ij')[0] # make k copies
scl = 0.5;
n=randn(N)*scl # generate k vectors
yy=y+n    # add noise to signal
# shadow plot
plot(t,yy)
plot(t,y);
xlabel(r'$t$',size=20)
ylabel(r'$f(t)+n$',size=20)
title(r'Plot of the data to be fitted')
grid(True)
show()
'''Data Generation Done'''
measurements = yy;


kf = kf.em(measurements, n_iter=5)
(smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)
(filtered_state_means, filtered_state_covariances) = kf.filter(measurements);
plot(t,smoothed_state_means,'b',label = 'Kalman Smoothed');
plot(t,filtered_state_means,'g',label = 'Kalman Filter');
plot(t,y,'b--',label = 'Original Function');
plot(t,yy,'r--',label = 'Erroneous data');
legend(loc = 'upper right');

show();
