#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	if not matrix:
		return matrix
	new = []
	for r in matrix:
		row = []
		for n in r:
			row.append(n**2)
		new.append(row)
	return new	
