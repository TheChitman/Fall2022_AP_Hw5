#in the name of Allah

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


#fig = plt.figure()

image = plt.imread("image.jpeg")

fig, ax = plt.subplots()

fig.set_facecolor('xkcd:red')
fig.set_size_inches(4.5,4)
#ax.imshow(image, extent=[0, 400, 0 ,300])

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)


plt.show()

plt.savefig('img.pdf')
