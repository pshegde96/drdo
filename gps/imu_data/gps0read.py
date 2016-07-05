from pylab import *
import os;

os.system('clear');
os.system('clear');

f = open('100831_155323_Gps0.log');
data = loadtxt('100831_155323_Gps0.log');

lat = data[:,5];
lon = data[:,6];
t1 = data[:,1];
t2 = data[:,0];
t = t2 + 10**-6*t1;

data = array([lat,lon,t],dtype = float64);
savetxt('data_gps0.txt',data);
print 'Latitude,Longitude and time data saved in data_gps0.txt';
