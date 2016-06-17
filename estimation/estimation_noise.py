from pylab import *

data = loadtxt('data.txt');

'''Generate Noise'''
N=data.size # no of data points
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

'''Add extra noise to one of the sensors(t2)'''

N = 60; #Number of noisy patches in the data-set to be added
length = 100; #average length of each noisy patch
change = 20;

indices = array(rand(N)*(data.size-2*length-1200),dtype = int)+1200;
for i in indices:
	# generate the data points and add noise
	scl = 1.5;
	n=randn(length,)*scl # generate k vectors
	t2[i:i+length] += n    # add noise to signal


''''''


c = array([t1,t2]);

##Estimating t2 from t1.
##Consider the previous M samples when calculating mean and covariance.
t2_est = [];
M = 1000; # M indicates how many previous samples to consider during estimation
u_t1 = mean(t1[0:M]);
u_t2 = mean(t2[0:M]);
C = array([c[0,0:M],c[1,0:M]]);
for i in range(M,t1.size):
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

'''Checking for noise faults'''
print size(where(array(stdev)>0.9)[0]);
