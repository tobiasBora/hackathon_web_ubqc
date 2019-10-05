from measurements import parity_meas

from cqc.pythonLib import CQCConnection, qubit

import random


#####################################################################################################
#
# measure each column
#

def measC0(q1,q2,node): # implements measurements for first column of observables on qubits q1, q2
	
	# measure XI
	anc = qubit(node) # initialize ancilla qubit
	q1.H() # flip first qubit to X eigenbasis
	q1.cnot(anc)
	q1.H() # flip first qubit back
	
	m0 = anc.measure() # measure ancilla in computational basis
	
	
	# measure -XZ
	anc = qubit(node) # initialize ancilla qubit
	q1.H() # flip first qubit to X eigenbasis
	q1.cnot(anc)
	q2.cnot(anc)
	q1.H() # flip first qubit back
	
	m1 = (anc.measure() + 1)%2 # result of measuring -XZ
	
	
	# measure IZ
	anc = qubit(node) # initialize ancilla qubit
	q2.cnot(anc)
	
	m2 = anc.measure() # measure ancilla in computational basis
	
	
	return m0,m1,m2
	


def measC1(q1,q2,node): # implements measurements for first column of observables on qubits q1, q2
	
	# measure XX
	anc = qubit(node)
	q1.H() # flip first qubit to X eigenbasis
	q2.H() # flip second qubit to X eigenbasis
	q1.cnot(anc)
	q2.cnot(anc)
	# flip both qubits back
	q1.H()
	q2.H()
	
	m0 = anc.measure() # measure ancilla in computational basis
	
	
	# measure YY
	anc = qubit(node)
	q1.K() # flip first qubit to Y eigenbasis
	q2.K() # flip second qubit to Y eigenbasis
	q1.cnot(anc)
	q2.cnot(anc)
	# IDK how to flip qubits back from Y to Z basis, since K is not self inverse
	
	m1 = anc.measure() # measure ancilla in computational basis
	
	
	# measure ZZ
	anc = qubit(node) # initialize ancilla qubit
	q1.cnot(anc)
	q2.cnot(anc)
	
	m2 = anc.measure() # measure ancilla in computational basis
	
	
	return m0,m1,m2

#####################################################################################################
#
# main
#
def main(col):
	
	
	# Initialize the connection
	with CQCConnection("Bob") as Bob:

		# Create EPR pairs
		q1=Bob.recvEPR()
		q2=Bob.recvEPR()

		# Make sure we order the qubits consistently with Alice
		# Get entanglement IDs
		q1_ID = q1.get_entInfo().id_AB
		q2_ID = q2.get_entInfo().id_AB

		if q1_ID < q2_ID:
			qb=q1
			qd=q2
		else:
			qb=q2
			qd=q1
		
		
		print("\n qb ids for bob",qb.get_entInfo().id_AB,"", qd.get_entInfo().id_AB,"\n")
		
		col = 0 
		
		# Perform the three measurements
		
		#if col == 0:
		#	qb.H()
		#	qd.H()
		#	m0 = qb.measure(inplace=True) + qd.measure(inplace=True)
		#	m1 = parity_meas([qb, qd], "ZZ", Bob, negative=True)
		#	m2 = parity_meas([qb, qd], "ZZ", Bob)
		
		if col == 0:
			m0,m1,m2 = measC0(qb,qd,Bob)
		'''if col == 0:
			m0 = parity_meas([qb, qd], "XI", Bob)
			m1 = parity_meas([qb, qd], "XZ", Bob, negative=True)
			m2 = parity_meas([qb, qd], "IX", Bob)
		elif col == 1:
			m0 = parity_meas([qb, qd], "XX", Bob)
			m1 = parity_meas([qb, qd], "YY", Bob)
			m2 = parity_meas([qb, qd], "ZZ", Bob)
		elif col == 2:
			m0 = parity_meas([qb, qd], "IX", Bob)
			m1 = parity_meas([qb, qd], "ZX", Bob, negative=True)
			m2 = parity_meas([qb, qd], "ZI", Bob)	'''
		
		print("Bob's results for column ",col," are ",m0," ",m1," ",m2)
			
		'''print("\n")
		print("==========================")
		print("App {}: column is:".format(Bob.name))
		print("(" + "_"*col + str(m0) + "_"*(2-col) + ")")
		print("(" + "_"*col + str(m1) + "_"*(2-col) + ")")
		print("(" + "_"*col + str(m2) + "_"*(2-col) + ")")
		print("==========================")
		print("\n")'''

		# Clear qubits
		qb.measure()
		qd.measure()




