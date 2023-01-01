import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

im = plt.imread("image.jpeg")

fig, ax = plt.subplots()
ax.set_ylim(-200, 200)
#ax.axis("off")



x = np.arange(0, 50*np.pi, 0.01)
line, = ax.plot(x, np.sin(x), color='black')

im = ax.imshow(im, extent=[100, 200, 100, 200])


def animate(i):
    line.set_ydata(np.sin(x + i/2.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)



plt.show()

#writer = PillowWriter(fps=2)
#ani.save("demo2.gif", writer=writer)