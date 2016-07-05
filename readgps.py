from pylab import *

f = open('gps1.plt');

lat = [];
lon = [];
for line in f:
	temp = '';
	for l in line:
		if l == ',':
			temp += ' ';
		else:
			temp += l;
	a,b,c,d,e,f,g = temp.split();	
	lat.append(float(a));
	lon.append(float(b));

data = array([lat,lon],dtype = float64);
savetxt('data_gps1.txt',data);
print 'Lat,Lon data written to data_gps1.txt';
