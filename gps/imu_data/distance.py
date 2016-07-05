from pylab import *
from pykalman import KalmanFilter

kf = KalmanFilter();
data = loadtxt('data_gps0.txt');
lat = radians(data[0,:]);
lon = radians(data[1,:]);
t = data[2,:];

dlat = lat[1:] - lat[0:-1];
dlon = lon[1:] - lon[0:-1];
dt = t[1:] - t[0:-1];

R = 6373; #Radius of earth in kilometers
a = (sin(dlat/2))**2 + cos(lat[0:-1])*cos(lat[1:])*((sin(dlon/2))**2);
c = 2*arctan2(sqrt(a),sqrt(1-a));
d = R * c;

#kf = kf.em(d,n_iter = 5);
#(smoothed_means,smoothed_cov) = kf.smooth(d);
#(filtered_means,filtered_cov) = kf.filter(d);

velocity = (1000*d)/dt;
velocity = (18.0/5)*velocity; #m/s to km/h
print max(velocity);
print min(velocity);
print sum(velocity)/len(velocity);
plot(velocity,label = 'Original Data');
#plot(smoothed_means,label = 'Kalman Smoothed');
#plot(filtered_means,label = 'Kalman Filtered');
legend();
show();
