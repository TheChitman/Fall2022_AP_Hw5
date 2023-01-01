#in the name of allah

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation

x = np.arange(0, 50*np.pi, 0.01)
y = np.sin(x)
plt.plot(x, y, color='black')
plt.ylim(20,-20)
#plt.axis('off')


plt.savefig("test.pdf")
