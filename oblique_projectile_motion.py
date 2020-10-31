import matplotlib.pyplot as plt
import numpy as np

#Functions
def trajectory_gravity(v0, kat_sin, kat_cos, H, g, Rz, k):
	''' Oblique projectile motion without air resistance.
	Variable gravity depending on distance form earth:
	g = g0*(Rz/(Rz + y))**2
	'''
	g0 = g * (Rz/(Rz + H))**2
	xt = [0]
	yt = [H]
	i = 0
	t = 0
	while yt[-1] > 0.01:
		g0 = g*(Rz/(Rz + yt[i]))**2
		xt.append(v0 * kat_cos * t)
		yt.append(H + v0 * kat_sin * t - 1/2 * g0 * t**2)
		i = i + 1
		t = t + 0.01
	plt.plot(xt, yt, k, label = 'v0 = ' + str(v0) + ' m/s^2' )
	x_max = max(xt)
	h_max = max(yt)
	return(t, x_max, h_max)

def plot_lines_and_title(name, H, x_max_list, h_max_list):
	''' The function draws plot and gives it a title.
	'''
	plt.plot([max(x_max_list), 0], [0, 0], 'k--', label = '_nolegend_')
	plt.plot([0, 0], [H, 0], 'k--', label = '_nolegend_')
	plt.title(name) 
	plt.legend()
	plt.xticks(x_max_list)
	plt.yticks(h_max_list)
	plt.xlabel('x [m]')
	plt.ylabel('y [m]')


# Data
H = 8
kat_sin = 1/2  	# 30 degrees
kat_cos = np.sqrt(3)/2
Rz = 6371 * 10**3
g = 9.81
color = 'rgbmkc'
v_0 = [8, 12, 14, 20]

#Drawing
i = 0
t_list = []
x_max_list = [0]
h_max_list = [H]
for v0 in v_0:
	i = i+1
	t, x_max, h_max = trajectory_gravity(v0, kat_sin, kat_cos, H, g, Rz, color[i])
	t_list.append(t)
	x_max_list.append(x_max)
	h_max_list.append(h_max)
for i in range(len(v_0)):
	print('The object thrown with the initial velocity v0 ='+
	' {a} m/s^2 was falling t = {b} seconds. '.format(a = v_0[i], b = round(t_list[i],2)))
plot_lines_and_title('Oblique projectile motion form height', H, x_max_list, h_max_list)
plt.show()
