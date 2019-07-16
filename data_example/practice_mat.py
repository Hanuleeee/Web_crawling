import numpy as np
from matplotlib import pyplot as plt

rand_array = np.random.randn(2,1000)
uni_array = np.random.rand(2,1000)*6-3

plt.plot(rand_array[0], rand_array[1],'ro')
plt.plot(uni_array[0],uni_array[1],'g.')

plt.show()
