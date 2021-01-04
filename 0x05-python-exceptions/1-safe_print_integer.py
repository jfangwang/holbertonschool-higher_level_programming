#!/usr/bin/python3
def safe_print_integer(value):
	try:
		print("{:d}".format())
		return value.isdigit()
	except (IndexError, TypeError, ValueError):
		return	False
