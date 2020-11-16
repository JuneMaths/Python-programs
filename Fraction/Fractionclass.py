
def gcd(m, n):		
	""" The function is calculating the gratest common divisor."""					
	while m%n != 0:		# This method is acceptable for our fraction class 
		oldm = m			# because we need to have negative fraction 
		oldn = n			# represented by a negative numerator.
		m = oldn			# Static method
		n = oldm % oldn	# This function have to be here because if it's below it's not defined.
	return n	

class Fraction:
	""" Fraction class was created to represent fractions.
		The class has implemented basic methods allownig operations on fractions.
	"""			
	def __init__(self, n = 1, d = 2):			# Default value of fraction is 1/2
		""" The function initialize Fraction class and handle exceptions."""
		if type(n)!= int or type(d)!= int:
			raise TypeError("You probably didn't type integer.")
		elif d == 0:
			raise ZeroDivisionError("Denominator can't be zero.")
		shorten = gcd(n, d)
		self.numerator = n // shorten		# There is "//" because the result must be integer not float.
		self.denominator = d // shorten		# When denominator is less than 0, operation shorten change negative denominator to positive one.
			
	def __str__(self):
		""" The function is needed to convert fraction into a string."""
		if self.numerator == 0:			# If numerator is zero, the fraction should be 0
			return "0"					# If denominator is less than zero, it's wrong to put minus after "/". We have to put it in the numerator.
		elif self.denominator == 1:
			return str(self.numerator)
		else:	
			return str(self.numerator) + "/" + str(self.denominator)	

	def __neg__(self):
		""" The function is needed to change the sing of the fraction"""
		return Fraction(-self.numerator, self.denominator)
			
	def __add__(self, other):
		""" The function is needed to add two fraction objects."""
		a = self.numerator
		b = self.denominator
		c = other.numerator
		d = other.denominator
		new_num = (a*d) + (c*b)
		new_den = (b*d) 
		return Fraction(new_num, new_den)
			
	def __sub__(self, other):
		""" The function is needed to subtract two fraction objects."""
		a = self.numerator
		b = self.denominator
		c = other.numerator
		d = other.denominator
		new_num = (a*d) - (c*b)
		new_den = (b*d) 
		return Fraction(new_num, new_den)
				
	def __mul__(self, other):
		""" The function is needed to multiply two fraction objects."""
		a = self.numerator
		b = self.denominator
		c = other.numerator
		d = other.denominator 
		return Fraction(a*c, b*d)
				
	def __truediv__(self, other):
		""" The function is needed to divide two fraction objects."""
		a = self.numerator
		b = self.denominator
		c = other.numerator
		d = other.denominator 
		return Fraction(a*d, b*c)

	def __eq__(self, other):
		""" The function is needed to check if two fraction objects are equal."""
		first = self.numerator * other.denominator		# Moving to the other side of the equation
		second = other.numerator * self.denominator
		return first == second
				
	def __ne__(self, other):
		"""The function is needed to check if two fraction objects are not equal."""
		first = self.numerator * other.denominator		
		second = other.numerator * self.denominator
		return first != second
				
	def __lt__(self, other):
		"""The function is needed to check if one fraction object is less than another one."""
		first = self.numerator * other.denominator		
		second = other.numerator * self.denominator
		return first < second
				
	def __gt__(self, other):
		"""The function is needed to check if one fraction object is greater than another one."""
		first = self.numerator * other.denominator		
		second = other.numerator* self.denominator
		return first > second
				
	def __le__(self, other):				
		"""The function is needed to check if one fraction object is less equal to another one."""
		first = self.numerator * other.denominator		
		second = other.numerator * self.denominator
		return first <= second
			
	def __ge__(self, other):
		"""The function is needed to check if one fraction object is greater equal to another one."""
		first = self.numerator * other.denominator		
		second = other.numerator * self.denominator
		return first >= second

	def getNum(self):
		"""The function return numerator from the fraction."""
		return self.numerator
				
	def getDem(self):
		"""The function return denominator from the fraction."""
		return self.denominator
		
	def decimal(self):
		"""The function change fraction into decimal fraction"""
		return self.numerator/self.denominator
