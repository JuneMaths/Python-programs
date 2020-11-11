class Stack:
	""" Stack is a collection of objects that supports fast last-in, first-out.
		In stack a new element is added at one end and an element is removed from 
		that end only. Stack uses operations like push and pop to add and remove 
		elements from stack. It is also possible to chceck first element on the stack 
		by method called peek and check the size of the stack or 
		if is it empty by using size and isEmpty. [Last-in, First-out]
	"""
	def __init__(self):
		""" The function inicialises a stack. It takes no arguments."""
		self.items = []

	def __str__(self):
		""" The function tells how to represent stack as a string. 
			It takes no arguments.
		"""
		return str(self.items)

	def isEmpty(self):
		""" The function checks if the stack is empty. It takes no argumnets. 
			The function return True or False.
		"""
		return self.items == []

	def push(self, item):
		""" The function adds element to the top of the stack. It takes one argument 
			which is adding element. A specific type of element is not needed.
		"""
		self.items.append(item)

	def pop(self):
		""" The function removes the first element from the top of the stack 
			and return it's value. It takes no argument.
		"""
		return self.items.pop()

	def peek(self):
		""" The function checks what element is to the top of the stack. 
			It takes no argument.
		"""
		return self.items[len(self.items) - 1]

	def size(self):
		""" The function checks the number of elements in the stack. 
			It takes no arguments.
		"""
		return len(self.items)