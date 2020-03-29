import numpy as np
import matplotlib.pyplot as plt
def genData(N,d,distribution="normal",**kwargs):
	if distribution == "normal":
		try:
			mean = kwargs['mean']
			stddev = kwargs['stddev']
		except KeyError:
			raise Exception("please insert the correct arg for normal distribution")
		assert(mean.shape[0] == d and stddev.shape[0] == d), "mean and stddev must have shape (d,)"
		return np.random.normal(loc=mean,scale=stddev,size=(N,d))
	if distribution == "uniform":
		try:
			low = kwargs['low']
			high = kwargs['high']
		except KeyError:
			raise Exception("missing lower or upper bound for distribution")
		assert(low.shape[0] == d and high.shape[0] == d), "lower and high must have shape (d,)"
		return np.random.uniform(low=low, high=high,size=(N,d))
	if distribution == "binomial":
		try:
			prob = kwargs['prob']
			n_trials = kwargs['n_trials']
		except KeyError:
			raise Exception("where is arguments for binomial distribution? ")
		assert(prob.shape[0] == d), " probabilities must have shape (d,)"
		return np.random.binomial(n=np.ones(shape=(d,)).astype(np.int32)*n_trials,p=prob,size=(N,d))
	else:
		return "well cant find your distribution here, maybe you can contribute a little to this problem?"


def avgSample(sample,w):
	# sample must have dim (samples_num,sample_dim)
	# w must have dim (1,samples_num)
	sum =0
	for i in w:
		sum += w
	return np.dot(w,sample)/ sum

def medianSample(sample,w):
	sum1 =0
	med_val = 0
	for i in w:
		sum1 += w
	j = 0
	while(med_val < sum1 /2.0):
		med_val += w[0,j]
		j+=1
	return sample[j-1]
def modeSample(sample,w):
	max1 = 0
	x = np.argmax(w)
	return sample[x]




