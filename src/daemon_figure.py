import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
from PIL import Image

Address_of_image = "../resources/image.jpeg"

fig, ax = plt.subplots()

ax.set_ylim(-140, 140)
fig.set_facecolor('xkcd:red')

# Adding Sine

x = np.arange(0, 150*np.pi, 0.01)
line, = ax.plot(x, np.sin(x), color='black', label="akbaraqa")
plt.axis("off")

# Adding and seting images (normal and gray)

im = plt.imread(Address_of_image)
im = ax.imshow(im, extent=[0, 400, -140, 140])

img2 = Image.open(Address_of_image).convert("L")
ax2 = fig.add_axes([0.7,0.65,0.2,0.2])
im2 = ax2.imshow(img2, cmap='gray',extent=[0, 50, -20, 20])
ax2.axis("off")

# set text

props = dict(boxstyle='round', facecolor='white', alpha=0.8)
ax.text(5, -125, "DAEMON",  fontsize=12, verticalalignment='top', bbox=props)

# _____ Start Animation Functionality ______

def animate(i):
    line.set_ydata(6*np.sin(x + i/2.0)) 
    return line,

def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)
# _____ End of Animation Functionality ______

plt.show()

# Saving to Gif

writer = PillowWriter(fps=5)
ani.save("../resources/wantedGif.gif", writer=writer)
