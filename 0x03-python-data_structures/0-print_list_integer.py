#!/usr/bin/python3
#0-print_list_integer.py


def print_list_integer(my_list=[]):
	""" A function that prints all the integer
	in a list.
	No modules should be imported
	Integers should not be casted into strings
	"""
	for i in my_list:
		print("{:d}".format(i))
