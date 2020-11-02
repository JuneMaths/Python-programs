import random
import functions_disk as fd		# My module
import matplotlib.pyplot as plt

def draw_disks(dyski, axs, sub_num, name = 'Name'):
	''' The function draws disks on the board
	'''
	ax = axs.flat[sub_num]
	ax.set(xlim = (-15, 15), ylim = (-15,15), title = name)
	for disc in dyski:
		circle = plt.Circle((disc['x'], disc['y']), disc['r'], color = disc['c'])
		ax.add_artist(circle)
	ax.set_aspect('equal', adjustable='box')


# Disks initializing
N = 100
dyski = []
for i in range(N):	# I randomize one hundred disks of radius 0.5
	dyski.append( {'x': random.uniform(-14.5, 14.5), 
	'y':random.uniform(-14.5, 14.5),'r': 0.5, 'c': 'm'} )

# Drawing disks
fig, axs = plt.subplots(1, 2)
draw_disks(dyski, axs, 0, 'Dyski przed usunięciem kolizji')

# Chart of uncorrelated disks
dyski_after = fd.push_apart_consolidated(dyski)
draw_disks(dyski_after, axs, 1, 'Dyski po usunięciu kolizji')
plt.show()
