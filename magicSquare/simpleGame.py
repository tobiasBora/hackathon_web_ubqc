#!/usr/bin/env python3
from cqc.pythonLib import CQCConnection, qubit


from measurements import parity_meas


import random

import alice, bob

#####################################################################################################

print("enter number of rounds")
rounds = int(input())

for r in range(rounds):
	
	print("\n")
	print("==========================")
	print("round ", r+1)
	print("==========================")
	print("\n")
	print("which row should Alice measure (0,1,2)")
	row = int(input())
	while not (row in range(3)):
		print("row should be 0, 1 or 2. Enter again.")
		row = int(input())
	
	print("which column should Bob measure (0,1,2)")
	col = int(input())
	while not (col in range(3)):
		print("column should be 0, 1 or 2. Enter again.")
		col = int(input())
	
	alice.main(row)
	bob.main(col)


