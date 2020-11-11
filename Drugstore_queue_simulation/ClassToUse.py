import random

class Client:
	def __init__(self, come_time, max_products):
		""" The function inicialize a Client class. It takes two arguents. The first 
			argument is a time when the client came and it sholud be intiger. 
			The second argument is a maximum products clients usually take in the shop.
		"""
		if type(come_time) == int and type(max_products) == int:
			self.come_time = come_time			# The amount of products from 1 do max_products
			self.products = random.randrange(1, max_products + 1)	
		else: 
			raise TypeError("types of both arguments sholud be intigers")

	def __str__(self):
		""" The function enable to show the element of Client class. 
			It takes no arguments.
		"""
		return str({'time':self.time, 'products':self.products})

	def get_come_time(self):
		""" The function returnes a time when the client came. 
			It takes no arguments.
		"""
		return self.come_time

	def get_products(self):
		""" The function retrunes a number of products the client took."""
		return self.products


class Cash_register:
	def __init__(self):
		""" The function inicialize a Cash_register class. 
		It takes no arguments.
		"""
		self.available = True

	def is_available(self):
		""" The function checks if cash register is available. It takes no arguments. 
			It returnes logical value.
		"""
		return self.available

	def set_available(self, log_value):
		""" The function set avaibility of cash register. It takes one argument 
			which is logical value.
		"""
		if type(log_value) == bool:
			self.available = log_value	
		else:
			raise TypeError("type of the argument sholud be bool")


class Self_checkout:
	def __init__(self):
		""" The function inicialize a Self_checkout class. It takes no arguments."""
		self.available = True

	def is_available(self):
		""" The function checks if self-checkout is available. It takes no arguments. 
			It returnes logical value.
		"""
		return self.available

	def set_available(self, log_value):
		""" The function set avaibility of self-checkout. It takes one argument 
			which is logical value.
		"""
		if type(log_value) == bool:
			self.available = log_value	
		else:
			raise TypeError("type of the argument sholud be bool")


class FrontaddQueue:
	""" Queue is a collection of objects that supports fast first-in,
		first-out semantics for inserts and deletes. In that queue
		the end of the queue is at the top of the list. Queue uses
		operations like enqueue and dequeue to add and to remove
		elements. It is also possible to check a size of the queue
		or if it is empty by methods size and isEmpty.
	"""
	def __init__(self):
		"""The function inicialises a queue. It takes no arguments."""
		self.items = []
		
	def __str__(self):
		""" The function tells how to represent queue as a string. 
			It takes no arguments.
		"""
		return str(self.items)
		
	def __getitem__(self, index):
		""" The function findes an element with a proper index. 
		It takes one argument which is the index of element.
		"""
		return self.items[index]
		
	def isEmpty(self):
		""" The function checks if the queue is empty. It takes 
			no argumnets. The function return True or False.
		"""
		return self.items == []
		
	def enqueue(self, item):
		""" The function adds element to the end of the queue. 
			It takes one argument which is adding element. 
			A specific type of element is not needed.
		"""
		self.items.insert(0, item)
		
	def dequeue(self):
		""" The function removes the first element from the front of 
			the queue and return it's value. It takes no argument.
		"""
		return self.items.pop()
		
	def size(self):
		""" The function checks the number of elements in the queue. 
			It takes no arguments.
		"""
		return len(self.items)

