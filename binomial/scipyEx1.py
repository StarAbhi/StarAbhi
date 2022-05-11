import numpy as np
import matplotlib.pyplot as plt
s=np.random.poisson(5, 10000)
plt.hist(s,16,normed=True,color='Green')
plt.show()