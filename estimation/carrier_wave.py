from pylab import *

t = arange(0,100,0.1);
x = sin(t);

r = rand(20);
b = ones(20);
i = where(r>0.5)[0];
b[i] = -1;
y = [];
binary = [];
for i in range(0,len(t)):
	index = i/50;
	y.append(x[i]*b[index]);
	binary.append(b[index]);

binary = array(binary);
y = array(y);

plot(t,y,'b');
plot(t,binary,'r');
show();

