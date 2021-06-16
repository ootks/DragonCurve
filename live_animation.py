import csv
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.animation as anim

log_n_points = 9

colors = cm.rainbow(np.arange(0, 1, 3**(-log_n_points)))

fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(-1.5, 2), ax.set_xticks([])
ax.set_ylim(-2, 2), ax.set_yticks([])
scat = ax.scatter(np.zeros(3**log_n_points), np.zeros(3**log_n_points), s=3, c=colors)

def transformation1(x, theta, phi):
    return np.array([[np.cos(theta), -np.sin(theta)],
                     [np.sin(theta), np.cos(theta)]]).dot(x) / np.sqrt(3)

def transformation2(x, theta, phi):
    y = np.array([[np.cos(phi + theta), -np.sin(phi + theta)],
                     [np.sin(phi + theta), np.cos(phi + theta)]]).dot(x) / np.sqrt(3) + np.array([1, 0])
    return y

def transformation3(x, theta, phi):
    y = np.array([[np.cos(2*phi), -np.sin(2*phi)],
                     [np.sin(2*phi), np.cos(2*phi)]]).dot(x) / np.sqrt(3) + np.array([0, 1])
    return y

transforms = [transformation1, transformation2, transformation3]

pts = [[-1,-1] for i in range(3**(log_n_points))]
def update(frame_number):
    print(frame_number/200.0)
    theta = 0.01 * (frame_number + 1)
    phi = 2 * np.sqrt(2) * theta

    pts[0] = [1,0]

    for i in range(log_n_points):
        for j in range(2, -1, -1):
            for k in range(3**i):
                pts[j*3**i+k]  = transforms[j](pts[k], theta, phi)

    scat.set_offsets(np.array(pts))

animation = anim.FuncAnimation(fig, update, frames=200, interval=10)
animation.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
