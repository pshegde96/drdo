from pylab import *

data = loadtxt('data.txt');
diff = data[1:]-data[0:-1];
N = 100;
stdev = [];
i = 0;
while True:
	if i+N > size(data):
		break;
	A = diff[i:i+N];
	stdev.append(abs(std(A)));
	i = i+N;

print "No of patches:";
print len(stdev);
print "Noisy patches:";
print size(where(abs(array(stdev))>1.2)[0]);


