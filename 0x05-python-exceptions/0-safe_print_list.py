def safe_print_list(my_list=[], x=0):
	count = 0


	try:
		for a in range(x):
			print("{:d}".format(my_list[a]), end=' ')
			count += 1
		print()
	except (IndexError, TypeError, AttributeError):
		print()
	finally:
		return count
