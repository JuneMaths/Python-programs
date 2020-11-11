
# DESCRIPTION OF SYMULATION:

# Let's assume that we are in a Rossmann. There are two opportunities. 
# You can pay in cash register or in self-checkout.
# Clients come to the shop and get products. 
# In average one customer takes from 1 to 15 products. 
# There is only one queue to both checkout desks.
# If one of them is avaiable, customer comes and pay. 
# In average in rush hours (15.00-18.00) there is around 
# 60 peopole per hour which gives 1 person per 60 second.
# In cash register paying takes 60 seconds and 1 product per 3 second. 
# (paying time + [getting product, beep, puting product])
# In self-checkout paying takes 80 seconds and 1 product per 4 second. 
# (paying time + [getting product, looking for barcode, beep, putting product])
# Statistically we are more willing to choose cash register, 
# because self-checkout is still unknown technology for most of people.

# What is the averge time of waiting to pay?
# Is it necessary to buy a new self-checkout or employ new cashier?.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import ClassToUse as ctu
import random


def new_client(seconds_per_person):
	""" The function control when the new client arrives. It can arrive any second. 
		Statistically it is one client in one minute. The function takes no anrguments. 
		It returnes True if new client arrives and False if not.
	"""
	sec = random.randrange(1, seconds_per_person + 1)	# 60 person per 1h is 1person per 60second
	if sec == seconds_per_person:
		return True
	else:
		return False


def symulation(rush_seconds, seconds_per_person, max_products):	
	""" The function is the main symulation of the program It takes two arguments. 
		The first argument is the time range when the symulation is conducted. 
		The second argument is a maximum of product which clients buy. 
		It returnes valuable informations about average waiting time.
	"""
	if type(rush_seconds) == int and type(max_products) == int:

		queue = ctu.FrontaddQueue()					# Inicialize the Queue.
		cash_register = ctu.Cash_register()			# Inicialize the Cash register.
		self_checkout = ctu.Self_checkout()			# Inicialize the Self-checkout.

		delay_cash = 0
		delay_self = 0
		amount_clients_cash = 0
		amount_clients_self = 0
		waiting_sum_cash = 0
		waiting_sum_self = 0

		for current_time in range(rush_seconds):			# 3h=10800s is rush hours.

			if new_client(seconds_per_person):				# If new client arrive, set his come_time and a maximum number of products.
				client = ctu.Client(current_time, max_products)
				queue.enqueue(client)						# He stand in queue.
				#print("new client with time:", current_time)	
															# Customers prefer Cash_register that's why it is first.
			if cash_register.is_available() and  not queue.isEmpty():			# If cash register is avaiable and someone is in the queue.
				customer = queue.dequeue()										# Customer comes to cash register.
				cash_register.set_available(False)
				delay_cash = current_time + 60 + 3 * customer.get_products()	# Customer is paying to that time.
				waiting_sum_cash = waiting_sum_cash + current_time - customer.get_come_time()
				amount_clients_cash = amount_clients_cash + 1
				#print("time:",current_time,"cash register serve customer with time:",
						#customer.get_come_time(), "to the time:", delay_cash )
				
			if self_checkout.is_available() and not queue.isEmpty():			# If self-checkout is avaiable and someone is in the queue.
				customer = queue.dequeue()										# Customer comes to self-checkout.
				self_checkout.set_available(False)
				delay_self = current_time + 80 + 4 * customer.get_products()	# Customer is paying to that time.
				waiting_sum_self = waiting_sum_self + current_time - customer.get_come_time()
				amount_clients_self = amount_clients_self + 1
				#print("time:",current_time,"self-checkout of customer with time:", 
						#customer.get_come_time(), "to the time:", delay_self )

			if current_time == delay_cash:			# If customer in cash register paid.
				#print("cash_register available")
				cash_register.set_available(True)	

			if current_time == delay_self:			# If customer in self-checkout paid.
				#print("self-checkout available")
				self_checkout.set_available(True)	

		average_cash = waiting_sum_cash / amount_clients_cash
		average_self = waiting_sum_self / amount_clients_self

		return [['Clients to serve:', queue.size()], 
				['Amount of customers:', '-cash register:', amount_clients_cash ,
				'-self-checkout:', amount_clients_self], [average_cash, average_self]]

	else:
		raise TypeError("type of both arguments sholud be intiger")


def average_days_waiting_times(days, rush_seconds, seconds_per_person, max_products):
	""" The function calls main symulation right number of times
		which correspond days in the shop.
	"""
	if type(days) == int:
		sum_cash = 0
		sum_self = 0
		client_cash_sum = 0
		client_self_sum = 0
		clients_left = 0
		for day in range(days):
			sum_cash = sum_cash + symulation(rush_seconds, seconds_per_person, max_products)[2][0]
			sum_self = sum_self + symulation(rush_seconds, seconds_per_person, max_products)[2][1]
			client_cash_sum = client_cash_sum + symulation(rush_seconds, seconds_per_person, max_products)[1][2]
			client_self_sum = client_self_sum + symulation(rush_seconds, seconds_per_person, max_products)[1][4]
			clients_left = clients_left + symulation(rush_seconds, seconds_per_person, max_products)[0][1]
		average_waiting = (sum_cash + sum_self) / (2 * days)
		return "In %i days statistically %i clients were served during one day and %i clients left." \
				" Average waiting time in queue is %0.2f seconds." \
				" Waiting time to cash register is %0.2f seconds and waiting time" \
				" to self-checkout is %0.2f seconds." % (days,  (client_cash_sum + client_self_sum) / days, 
				clients_left / days ,average_waiting, sum_cash / days, sum_self / days)
	else:
		raise TypeError("type of the argument sholud be intiger")


days = 31
rush_seconds = 10800	# 3h ruch hours
seconds_per_person = 60
max_products = 15
print(average_days_waiting_times(days,rush_seconds, seconds_per_person, max_products))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print()
# We can notice that avarage time the customer spends in waiting queue 
# for both cash register and self-checkout is less than 3 minutes 
# which is not too much. But if we consider that Rossmann ususally 
# reduce prices twice a year our model isn't right.
# In that time number of customers incrise to 1 client in 45 seconds.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

days = 31
rush_seconds = 10800
seconds_per_person = 45
max_products = 15
print(average_days_waiting_times(days,rush_seconds, seconds_per_person, max_products))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# There are too many customes to serve left. And waiting time in queue 
# incrises to around 8 minutes. In conlusion the shop sholud add a cashier 
# diuring this time or sholud buy additional self-checkout. . 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
