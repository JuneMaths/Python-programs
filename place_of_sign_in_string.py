# The program finds a position of any sign in a sentence. 
# It returns a number of the sign in the sentence and positions of the sign.
# It plots histogram of numbers of every signs in the sentence. 

# Example of a sentence:
# Jeżeli powiecie dorosłym: "Dowodem istnienia Małego Księcia jest to, że był śliczny, że śmiał się i że chciał mieć baranka, a jeżeli chce się mieć baranka, to dowód, że się istnieje" - wówczas wzruszą ramionami i potraktują was jak dzieci. Lecz jeżeli im powiecie, że przybył z planety B-612, uwierzą i nie będą zadawać niemądrych pytań. Oni są właśnie tacy. Nie można od nich za dużo wymagać. Dzieci muszą być bardzo pobłażliwe w stosunku do dorosłych. 

import matplotlib.pyplot as plt
import numpy as np


def find_the_sign(x, sentence):
	''' The function...
	'''
	number = 0
	sign_position = []
	for i in range (len(sentence)):	# for don't take the last iteration
		if  sentence[i] == x:
			sign_position.append(i)	# Saving position of the sign counting from 0
			number = number + 1		# Counting how many signs were found
	# Output information
	if number == 0:	
		print('The sign',x, 'was not found in the sentence.')
	else:
		if number == 1:
			print('Sign "', x, '" appears in the string 1 time on the position',
				sign_position,'counting from 0.')
		else:
			print('Sign "', x, '" appears in the string', 
				number, 'times on the position',
				sign_position,'counting from 0.')	
	return None		
		
		
def histogram_sign(sentence):
	''' The function...
	'''
	sign_list = []
	for i in sentence:	# Filters existing signs
		if i not in sign_list:
			sign_list.append(i)
	amount = []
	for i in sign_list: # Amount of every sign
		amount.append(sentence.count(i))
	plt.bar( np.arange(len(sign_list)),amount, facecolor='black', edgecolor='grey')
	plt.xticks(np.arange(len(sign_list)), sign_list)
	for i in range(0, len(sign_list)):
		plt.text(i -0.25, amount[i]+0.05*max(amount), str(amount[i]))
	plt.title('Histogram of signs in sentence')
	plt.xlabel('sign')
	plt.ylabel('number of sign')
	plt.ylim([0, max(amount)+0.15 * max(amount)])
	plt.show()
	
	
sentence = input('Enter the selected string: ')
sentence = sentence.lower()

length = len(sentence)-1
if length >= 0:			# Sentence have to be entered
	x = input('Enter the sign you are looking for: ')
	x = x.lower()
	if len(x) == 1:		# It should be only one sign
		find_the_sign(x, sentence)
		histogram_sign(sentence)
	else:
		raise ValueError('you can enter only one sign')	
else:
	raise ValueError('you should enter a sentence')
