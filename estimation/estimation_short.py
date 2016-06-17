from pylab import *

data = loadtxt('data.txt');
length = size(data);

'''Generate Noise'''
N=length # no of data points
k=2   # no of sets of data with varying noise
# generate the data points and add noise
Y=meshgrid(data,ones(k),indexing='ij')[0] # make k copies
scl = [0.5,0.5];
n=dot(randn(N,k),diag(scl)) # generate k vectors
yy=Y+n    # add noise to signal
'''End generation of noise'''

##Separate the signal as signal from two sensors
t1 = transpose(yy[:,0]);
t2 = transpose(yy[:,1]);

'''Add the short faults to one of the sensors(t2)'''

intensity = 0.5;

#Get the index for 100 randomly selected samples
index = rand(500);
index = array(index*(data.size-1200),dtype = int)+1200;#Make sure there are no faults in the first 1000 samples as they are used to estimate future values
print where(index < 1200)[0];
#print index;
t2[index] = t2[index] + intensity*t2[index];


''''''
c = array([t1,t2]);

##Estimating t2 from t1.
##Consider the previous M samples when calculating mean and covariance.
t2_est = [];
M = 1000; # M indicates how many previous samples to consider during estimation
u_t1 = mean(t1[0:M]);
u_t2 = mean(t2[0:M]);
C = array([c[0,0:M],c[1,0:M]]);
for i in range(M,length):
#	u_t1 = mean(t1[i-M:i]);
#	u_t2 = mean(t2[i-M:i]);
#	C = array([c[0,i-M:i],c[1,i-M:i]]);
	covar = cov(C);
	t2_est.append(u_t2 + (covar[1,1]/covar[0,0])*(t1[i]-u_t1));
t2_est = array(t2_est);

diff = abs(t2_est - t2[M:]);
print std(diff);

###Show the results
N = 100; # N is the number of samples to be clumped together during calculation of stdev
stdev = [];
i = 0;
while True:
	if i+N > size(diff):
		break;
	A = diff[i:i+N];
	stdev.append(abs(std(A)));
	i = i+N;
hist(stdev,100);
show();

plot(t2[M:M+100],'b',label = 'True Sensor Value');
plot(t2_est[0:100],'g',label = 'Estimated Sensor Value');
legend(loc = 'upper right');
show();

'''Checking for short faults'''
threshold = 5;
i = 0;
short_count = 0;
ind = [];
while i<diff.size:
	if diff[i] > threshold: #Occurence of short fault
		short_count += 1;
		ind.append(i+1);
		#Go through all the samples that are part of the same short-fault
		i = i +1;
		while (i<diff.size):
			if diff[i] > threshold:
				break;
			i = i+1;
	else :
		i = i+1;
print short_count;
#print array(index);
#print diff[array(index)-M];


''''''

