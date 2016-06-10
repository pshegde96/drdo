from pylab import *
from pykalman import KalmanFilter

data = loadtxt('data.txt');
length = size(data);

'''Generate Noise'''
from pylab import *
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
#plot(t1);
#plot(t2);
#show();

##Apply Kalman smoothing to the two signals[Consider only first 10000 samples]
Size = 10000;
t1 = t1[0:Size];
t2 = t2[0:Size];
kf1 = KalmanFilter();
kf1 = kf1.em(t1,n_iter = 5);
(t1,covariance) = kf1.smooth(t1);
kf2 = KalmanFilter();
kf2 = kf2.em(t2,n_iter = 5);
(t2,covariance) = kf2.smooth(t2); 
plot(t1);
plot(t2);
show();

t1 = transpose(t1);
t1 = t1.reshape(Size);
t2 = transpose(t2);
t2 = t2.reshape(Size);
c = array([t1,t2]);
print corrcoef(c);

##Estimating t2 from t1.
##Consider the previous M samples when calculating mean and covariance.
t2_est = [];
M = 100; # M indicates how many previous samples to consider during estimation
for i in range(M,size(t1)):
	u_t1 = mean(t1[i-M:i]);
	u_t2 = mean(t2[i-M:i]);
	C = array([c[0,i-M:i],c[1,i-M:i]]);
	covar = cov(C);
	t2_est.append(u_t2 + (covar[1,1]/covar[0,0])*(t1[i]-u_t1));
t2_est = array(t2_est);

diff = t2_est - t2[M:];
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

