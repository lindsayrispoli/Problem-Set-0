import ps0

#Test case for number 0
print("The number 6 is {}.".format(ps0.odd_even(6)))
print("The number 5 is {}.".format(ps0.odd_even(5)))
print("The number 0 is {}.".format(ps0.odd_even(0)))

#Test case for number 1
print("The number 56 has {} digits.".format(ps0.number_digits(56)))
print("The number 0 has {} didgits.".format(ps0.number_digits(0)))
print("The number 12345 has {} digits.".format(ps0.number_digits(12345)))

#Test case for number 2
print("The sum of the digits of 56 is {}".format(ps0.sum_digits(56)))
print("The sum of the digits of 1234 is {}".format(ps0.sum_digits(1234)))
print("The sum of the digits of 0 is {}".format(ps0.sum_digits(0)))

#Test case for number 3 
print("The sum of the integers less than the given number 3 is {}".format(ps0.sum_less_number(3)))
print("The sum of the integers less than the given number 5 is {}".format(ps0.sum_less_number(5)))
print("The sum of the integers less than the given number 0 are {}".format(ps0.sum_less_number(0)))

#Test case for number 4
print("3 factorial is: {}".format(ps0.factorial(3)))
print("5 factorial is: {}".format(ps0.factorial(5)))
print("0 factorial is: {}".format(ps0.factorial(0)))

#Test case for number 5
print("6 is a factor of 3, which is {}".format(ps0.factor_of_first(6, 3)))
print("3 is a factor of 6, which is {}".format(ps0.factor_of_first(3, 6)))


#Test case for number 6
print("The number 5 is prime, which is {}".format(ps0.is_prime(5)))
print("The number 4 is prime, which is {}".format(ps0.is_prime(4)))
print("The number 9 is prime, which is {}".format(ps0.is_prime(9)))

#Test case for number 7
print("7 is a perfect number, which is {}".format(ps0.perfect_number(7)))
print("6 is a perfect number, which is {}".format(ps0.perfect_number(6)))
print("0 {}".format(ps0.perfect_number(0)))

#Test case for number 8
print("The sum of the digits of 123 divides evenly into 123, is {}".format(ps0.sum_divides_evenly(123)))
print("The sum of the digits of 3 divides evenly into 3, is {}".format(ps0.sum_divides_evenly(3)))
print("The sum of the digits of 0 divides evenly into 0, gives an {}".format(ps0.sum_divides_evenly(0)))