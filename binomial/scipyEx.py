import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1234)
samples=np.random.lognormal(mean=1.,sigma=.4,size=10000)
shape,loc,scale=scipy.stats.lognorm.fit(samples,floc=0)
num_bins=50
clr="#EFEFEF"
counts,edges,patches=plt.hist(samples,bins=num_bins,color=clr)
centers=0.5*(edges[:-1]+edges[1:])
cdf=scipy.stats.lognorm.cdf(edges,shape,loc=loc,scale=scale)
prob=np.diff(cdf)
plt.plot(centers,samples.size*prob,'k-',linewidth=2)
plt.show()