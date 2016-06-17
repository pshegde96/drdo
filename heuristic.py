from pylab import *

data = loadtxt('data_short.txt');
index_short = loadtxt('index_short.txt');


##Algorithm for automatic threshold detection
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


'''Detecting short faults'''
#threshold = 1.8*max(stdev);
threshold = 5;
diff = data[1:]-data[0:-1];
i = 0;
short_count = 0;
index = [];
while i<diff.size:
	if diff[i] > threshold: #Occurence of short fault
		short_count += 1;
		index.append(i+1);
		#Go through all the samples that are part of the same short-fault
		i = i +1;
		while (i<diff.size):
			if diff[i] > threshold:
				break;
			i = i+1;
	else :
		i = i+1;
print short_count;

'''
correct_count = 0;
for i in index_short:
	if i in index:
		correct_count += 1;
		
print correct_count;
'''

'''Detecting Noise faults'''

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
print where(array(stdev) > 1.5)[0].size;
