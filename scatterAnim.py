import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

np.random.seed(19680801)
data = {
    'a': np.random.randint(0, 50, 50),
    'c': np.random.rand(50, 4),
    'd': np.linspace(0,3,50)
}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(15, 8.1), layout='constrained')
scat = ax.scatter('a'[0], 'b'[0], c='c'[0], s='d'[0], data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')

def update(frame):
    x = data['a'][:frame]
    y = data['b'][:frame]
    g = data['c'][:frame]
    t = data['d'][:frame]

    scat.set_offsets(np.stack([x, y]).T)
    scat.set_sizes(t)
    scat.set_color(g)
    return scat

ani = anim.FuncAnimation(fig=fig, func=update, frames=50, interval=30)
plt.show()