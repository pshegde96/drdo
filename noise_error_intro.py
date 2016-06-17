from pylab import *

data = loadtxt('data.txt');

N = 20; #Number of noisy patches in the data-set to be added
length = 100; #average length of each noisy patch
change = 20;

'''Adding the noise'''
data_noisy = data;
indices = array(rand(N)*(data.size-2*length),dtype = int);
for i in indices:
	# generate the data points and add noise
	scl = 1.5;
	n=randn(length,)*scl # generate k vectors
	data_noisy[i:i+length] += n    # add noise to signal

#plot(data_noisy[indices[1]-100:indices[1]+220]);
#show();

savetxt('data_noise.txt',data_noisy);






