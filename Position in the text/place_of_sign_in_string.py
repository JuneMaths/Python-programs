# The program finds a position of any sign in a sentence. 
# It returns a number of how maany times the sign appears in the sentence 
# and it returnes the specufic positions of this sign.
# It plots histogram czestosc of every signs in the sentence. 

# Example of a sentence:
# Jeżeli powiecie dorosłym: "Dowodem istnienia Małego Księcia jest to, że był śliczny, że śmiał się i że chciał mieć baranka, a jeżeli chce się mieć baranka, to dowód, że się istnieje" - wówczas wzruszą ramionami i potraktują was jak dzieci. Lecz jeżeli im powiecie, że przybył z planety B-612, uwierzą i nie będą zadawać niemądrych pytań. Oni są właśnie tacy. Nie można od nich za dużo wymagać. Dzieci muszą być bardzo pobłażliwe w stosunku do dorosłych. 

import matplotlib.pyplot as plt
import numpy as np


def find_the_sign(x, sentence):
	''' The funnction is looking for a specyfic sign "x" in a sentance. 
		It takes two arguments. The first one is the sign 
		and the secand one is the sentence. It prints specyfic information. 
		It returnes None.
	'''
	number = 0
	sign_position = []
	for i in range(len(sentence)):		# for don't take the last iteration
		if sentence[i] == x:
			sign_position.append(i)		# Saving position of the sign counting from 0
			number = number + 1			# Counting how many signs were found
	# Output information
	if number == 0:
		print('The sign', x, 'was not found in the sentence.')
	else:
		if number == 1:
			print('Sign "', x, '" appears in the string 1 time on the position', 
				sign_position, 'counting from 0.')
		else:
			print('Sign "', x, '" appears in the string', number, 'times on the position', 
				sign_position, 'counting from 0.')	
	return None		


def histogram_sign(sentence):
	''' The function plots a histogram of czestość of every dign in the sentance. 
		It takes one argument which is the sentence. It returns None.
	'''
	sign_list = []
	for i in sentence:		# Filters existing signs
		if i not in sign_list:
			sign_list.append(i)
	amount = []
	for i in sign_list: 	# Amount of every sign
		amount.append(sentence.count(i))
	x_range = np.arange(len(sign_list))
	plt.bar(x_range, amount, facecolor = 'black', edgecolor = 'grey')
	plt.xticks(x_range, sign_list)
	for i in range(0, len(sign_list)):
		plt.text(i - 0.25, amount[i] + 0.05 * max(amount), str(amount[i]))
	plt.title('Histogram of signs in sentence')
	plt.xlabel('the sign')
	plt.ylabel('number of the sign')
	plt.ylim([0, max(amount) + 0.15 * max(amount)])
	plt.show()
	return None


sentence = input('Enter the selected string: ')
sentence = sentence.lower()
length = len(sentence) - 1
if length >= 0:				# Sentence have to be entered
	x = input('Enter the sign you are looking for: ')
	x = x.lower()
	if len(x) == 1:			# It should be only one sign
		find_the_sign(x, sentence)	# first defined function
		histogram_sign(sentence)	# second defined function
	else:
		raise ValueError('you can enter only one sign')	
else:
	raise ValueError('you should enter a sentence')
