import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,1001)
fx = 3*x+1

plt.plot(x, fx)
plt.savefig('output.png')
