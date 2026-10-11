import matplotlib.pyplot as plt
import numpy as np

x = np.array([22,7,1001])
fx = 3*x+1

plt.plot(x, fx)
plt.savefig('output.png')
