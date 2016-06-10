from pykalman import KalmanFilter
from pylab import *
#kf = KalmanFilter(transition_matrices = [[1, 1], [0, 1]], observation_matrices = [[0.1, 0.5], [-0.3, 0.0]])

kf = KalmanFilter()
#measurements = array([[1,0], [0,0], [0,1]])  # 3 observations

'''Gathering Data'''
measurements = loadtxt('data.txt')[0:500];
'''Data Gathering Done'''




kf = kf.em(measurements, n_iter=5)
(smoothed_state_means, smoothed_state_covariances) = kf.smooth(measurements)
plot(smoothed_state_means);
plot(measurements,'r--');
show();
