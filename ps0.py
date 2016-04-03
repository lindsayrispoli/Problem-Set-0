#0. Write a boolean function that takes in a positive integer or zero as a parameter
#Returns whether the number is odd or even.
def odd_even(integer):
	""" Tells if an integer is odd or even """
	if integer % 2 == 0: #See if there is a remainder 
		return True #even
	else: 
		return False #odd
		
#1. Write a function that takes a non-negative integer as a parameter
# Returns the number of digits in it.
def number_digits(integer):
	""" Tells the number of digits in a number"""
	length = 0
	if integer == 0:
		length = 1
	while integer > 0:
		length += 1
		integer = integer // 10
	return length

	
#2. Write a function that takes a non-negative integer as a parameter
#Returns the sum of its digits.
def sum_digits(integer):
	"""Tells the sum of the digits in a number"""
	final = 0
	while integer > 0:
		remainder = integer % 10 #The remainder is the first number
		final += remainder 
		integer = integer // 10
	return final
	
#3. Write a function that takes a non-negative integer as a parameter
#Returns the sum of all the integers that are less than the given number. 
def sum_less_number(integer):
	"""Gives the sum of the integers less than the given number"""
	final = 0
	while integer > 0:
		integer = integer - 1
		final += int(integer)	
	return final 	
		

#4. Write a function that takes a non-negative integer as a parameter
#Returns its factorial.  
def factorial(integer):
	"""the factorial of a number"""
	final = 1
	while integer > 0:
		final = final * int(integer) 
		integer = integer - 1
	return final 	
			
#5.Write a boolean function that takes two positive integers as parameters
#Figures out whether the second number is a factor the first.
def factor_of_first(integer1, integer2):
	"""Tells if the second number is a factor of the first"""
	if integer2 % integer1 == 0:
		return True
	else:
		return False


#6. Write a boolean function that takes an integer greater than or equal to 2
#Returns whether the number is a prime.
def is_prime(integer):
	"""Tells if the number is prime """
	for factor in range (2, integer): #looks at the number between 2 and the integer 
		if integer % factor == 0: 				
			return False
		else:
			return True
		

#7.Write a boolean function that takes a positive integer
#Returns whether the number is perfect.
# 6 is perfect because. Add all the factors  
def perfect_number(integer):	
	""" Tells if the number is perfect"""
	final = 0
	for number in range (1, integer): #looks at all number between 1 and integer
		if int(integer) % int(number) == 0:
			final += int(number) 
		number = integer - 1
	if final == integer:
		return True
	else:
		return False 

#8. Write a boolean function that takes a positive integer
#Returns true if the sum of the digits of the number divides evenly into the number, false otherwise 
def sum_divides_evenly(integer):
	"""Tells if the sum of the digits of a number divides evenly into the number """
	final = sum_digits(integer)
	if final % integer == 0:
		return True				
	else:
		return False 




	

 