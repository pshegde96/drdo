from pykalman import KalmanFilter
from pylab import *
kf = KalmanFilter()

#Load the data
data = loadtxt('data_gps1.txt');
lat = data[1,:];
t = array(range(0,len(lat)));

print len(lat);

kf = kf.em(lat, n_iter=5)
(smoothed_state_means, smoothed_state_covariances) = kf.smooth(lat)
(filtered_state_means, filtered_state_covariances) = kf.filter(lat);
plot(t,smoothed_state_means,'b',label = 'Kalman Smoothed');
plot(t,filtered_state_means,'g',label = 'Kalman Filter');
plot(t,lat,'b--',label = 'Original Function');
legend(loc = 'lower right');
ylim(min(lat),max(lat));
show();
