import Stackclass as stc

def is_correct(file):
	""" The function checks the syntax of the HTML document 
		for missing closing tags. It takes one argument which is HTML file 
		and return True if program is correct or False if it is not correct.
	"""
	try:
		stos = stc.Stack()
		text = open(file).read()
		exeptions = ['<!doctype html>', '<meta charset="UTF-8"/>', '<img src="" border="x">',	
					'<!-- komentarz -->', '<br>']	# Defining exception which don't have closing tag.
		while len(text) > 0:
			x1 = text.index('<')	
			x2 = text.index('>')
			exception = text[x1:x1+4]		# Looking for exceptions which have some arguments inside and are not constant.
			if text[x1:x2+1] in exeptions or exception == '<img' or exception == '<!--':
				text = text[x2+1:]			# Going forward in text.
			elif not stos.isEmpty() and stos.peek() == text[x1:x2+1]: 	# If the same tag is on the stack.
				stos.pop()
				text = text[x2+1:]
			else:
				tag = text[x1:x2+1]
				tag = tag.split(" ")		# Converting tags which have id or class and adding '/'.
				if len(tag) > 1:
					tag = tag[0] + '>'		# If there is spliting.
				else:						# If there is no spliting.
					tag = tag[0]
				stos.push(tag[0] + '/' + tag[1:])	# Adding converted tag to the stack
				text = text[x2+1:]
		if stos.isEmpty():					# Returning proper logical value.
			return(True)
		else:
			return False
	except (FileNotFoundError):
		return ("File not found.", file)

def file_informaion(file):
	""" The function gives output information about the file.
		It takes one argument which is HTML file.
	"""
	print("Is file '", file, "' correct?:", is_correct(file))
	

file_informaion('plikhtml0.txt')
file_informaion('plikhtml1.txt')
file_informaion('plikhtml2.txt')
file_informaion('plikhtml3.txt')
file_informaion('plikhtml3.txt')
