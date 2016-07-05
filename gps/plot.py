from pylab import *

data = loadtxt('data_gps1.txt');
lat = data[0,:];
lon = data[1,:];

diff = abs(lat[1:] - lat[0:-1]);

plot(diff);
show();
