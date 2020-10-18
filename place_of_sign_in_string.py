# The program find a position of any sign in a string from given position to given position. 
# It starts counting from 0.

sentence = input('Enter the selected string: ')
sentence = sentence.lower()

length = len(sentence)-1
if length >= 0:			# Sentence have to be entered
	x = input('Enter the sign you are looking for: ')
	x = x.lower()
	if len(x) == 1:		# It should be only one sign
		number = 0
		print('The scope of search is from 0 to', length)
		try:
			start = int(input('Enter the position where you want to start searching: '))
			end = int(input('Enter the position where you want to end searching: '))		
		except:
			raise TypeError('you should enter an integer')
		
		# Main condition and mechanism
		if start <= end and end <= length and start >= 0: # 0 <= start <= end <= length
			sign_position = []
			for i in range (start, end+1):	# for don't take the last iteration
				if  sentence[i] == x:
					sign_position.append(i)	# Saving position of the sign counting from 0
					number = number + 1		# Counting how many signs were found
		else:
			raise ValueError('you are out of scale')
		
		# Output information
		if number == 0:	
			print('The sign',x, 'was not found in the sentence.')
		else:
			if number == 1:
				print('Sign', x, 'appears in the string', 
					sentence.count(x.lower()), 'time on the position',
					sign_position,'counting from 0.')
			else:
				print('Sign', x, 'appears in the string', 
					sentence.count(x.lower()), 'times on the position',
					sign_position,'counting from 0.')
					
	else:
		raise ValueError('you can enter only one sign')
else:
	raise ValueError('you should enter a sentence')
