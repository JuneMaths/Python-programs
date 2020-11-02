import math 
import matplotlib.pyplot as plt
import random

def if_collision_between(d1, d2):
	''' The function detects a collision between two disks
	'''
	AB = math.sqrt((d1['x'] - d2['x'])**2 + (d1['y'] - d2['y'])**2) # distance between disks
	r1_suma_r2 = d1['r'] + d2['r']
	r1_minus_r2= abs(d1['r'] - d2['r'])
	if r1_minus_r2 > AB:					# internally disconnectable disks
		return True
	if r1_minus_r2 <= AB < r1_suma_r2:		# disks intersect or internally tangent
		return True
	if AB >= r1_suma_r2:					# disks separable or internally tangent
		return False

def move_vector(dysk, wektor):
	''' The function moves the disk by any vector
	'''
	new = {'x':0,'y':0,'r':0,'c':'b'}
	new['x'] = dysk['x'] + wektor['x']
	new['y'] = dysk['y'] + wektor['y']
	new['r'] = dysk['r']
	return new
	
def push_apart_consolidated(dyski):
	''' The function detects a collision between disks 
		and spreads the consolidated ones.
	'''
	k = 0
	kol = 1
	while kol > 0:
		k = k + 1	
		kol = 0		# number of colisions
		for i in range(len(dyski)):				# I compare each pair of disks with each other
			for j in range(i + 1, len(dyski)):	# i + 1 because I don't want to double-check the same pair of disks
				if if_collision_between(dyski[i], dyski[j]) == True:
					kol = kol + 1
					bin = random.randint(0, 1)
					if dyski[i]['x'] > 13:
						if bin == 0:
							dyski[i] = move_vector(dyski[i], {'x':-1 ,'y':-0.5})
						else:
							dyski[i] = move_vector(dyski[i], {'x':-0.5 ,'y':-1})
					if dyski[i]['y'] > 13:
						if bin == 0:
							dyski[i] = move_vector(dyski[i], {'x':-0.5, 'y':-1})
						else:
							dyski[i] = move_vector(dyski[i], {'x':-0.5 ,'y':-1})
					else:
						dyski[i] = move_vector(dyski[i], {'x':0.5, 'y':0.5})	
		print('The', k, 'iteration:', kol, 'collisions were detected')
	return dyski