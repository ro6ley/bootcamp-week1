import unittest
from prime_numbers import *


class PrimeNumbersTest(unittest.TestCase):
	""" Test cases for the function to generate prime numbers """
	def test_if_result_is_a_list(self):
		""" Check whether the result is a list """
		result = prime_numbers_generator(12)
		self.assertTrue(result, list)

	def test_empty_list_if_n_less_than_two(self):
		""" Check whether an empty list is returned if there are no
		prime numbers within the range provided """
		pass

	def test_raises_error_if_n_not_int(self):
		""" Check whther an error is returned if n is not an integer """
		pass

	def test_if_twenty_three_is_prime(self):
		""" Check whether 23 in the list of prime numbers generated """
		result = prime_numbers_generator(24)
		self.assertIn(23, result)