from pylab import *

data = loadtxt('data.txt');
diff = data[1:]-data[0:-1];
N = 1000;
stdev = [];
i = 0;
while True:
	if i+N > size(data):
		break;
	A = diff[i:i+N];
	stdev.append(abs(std(A)));
	i = i+N;
hist(stdev,100);
show();
print size(where(abs(diff)>2.0)[0]);
