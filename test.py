import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.cm as cm

colors = cm.rainbow(np.arange(0, 1, 2**(-14)))

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(-1.5, 2), ax.set_xticks([])
ax.set_ylim(-2, 2), ax.set_yticks([])
# Construct the scatter which we will update during animation
# as the raindrops develop.
scat = ax.scatter(np.zeros(2**13), np.zeros(2**13), s=3, c=colors)


def update(frame_number):
    offsets = np.genfromtxt("data/data{}.csv".format(frame_number + 1), delimiter=',', skip_header=1)
    scat.set_offsets(offsets)
    return scat


# Construct the animation, using the update function as the animation
# director.
animation = anim.FuncAnimation(fig, update, frames=209, interval=10)
animation.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()

