import numpy as np
import csv
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-1.5, 2), ylim=(-2, 2))
line, = ax.plot([], [], '.', markersize=1)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    with open("data/data{}.csv".format(i + 1)) as f:
        reader = csv.reader(f ,delimiter = ",")
        next(reader, None)
        x = []
        y = []
        for row in reader:
            x.append(float(row[0]))
            y.append(float(row[1]))
        line.set_data(np.array(x), np.array(y))
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=209, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
