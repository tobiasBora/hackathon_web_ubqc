from cqc.pythonLib import CQCConnection, qubit


#from SimulaQron.toolbox.measurements import parity_meas

from measurements import parity_meas

import random


#####################################################################################################
#
# measure each row
#


def measR0(q1,q2,node): # implements measurements for first row of observables on qubits q1, q2
	
	# measure XI
	anc = qubit(node)
	q1.H() # flip first qubit to X eigenbasis
	q1.cnot(anc)
	q1.H() # flip first qubit back
	
	m0 = anc.measure() # measure ancilla in computational basis
	
	
	# measure XX
	anc = qubit(node)
	q1.H() # flip first qubit to X eigenbasis
	q2.H() # flip second qubit to X eigenbasis
	q1.cnot(anc)
	q2.cnot(anc)
	# flip both qubits back
	q1.H()
	q2.H()
	
	m1 = anc.measure() # measure ancilla in computational basis
	
	# measure IX
	anc = qubit(node)
	q2.H() # flip second qubit to X eigenbasis
	q2.cnot(anc)
	q2.H() # flip second qubit back
	
	m2 = anc.measure() # measure ancilla in computational basis
	

	
	
	return m0,m1,m2



#####################################################################################################
#
# main
#
def main(row):

	# Initialize the connection
	with CQCConnection("Alice") as Alice:
	
			
		# Create EPR pairs
		q1 = Alice.createEPR("Bob")
		q2 = Alice.createEPR("Bob")

		# Make sure we order the qubits consistently with Bob
		# Get entanglement IDs
		q1_ID = q1.get_entInfo().id_AB
		q2_ID = q2.get_entInfo().id_AB

		if q1_ID < q2_ID:
			qa = q1
			qc = q2
		else:
			qa = q2
			qc = q1
			
			
		print("\n qb ids for alice",qa.get_entInfo().id_AB,"", qc.get_entInfo().id_AB,"\n")
		
		row =0
		
		# Perform the three measurements
		#if row == 0:
		#	qa.H()
		#	qc.H()
		#	m0 = qa.measure(inplace=True) + qc.measure(inplace=True)
		#	m1 = parity_meas([qa, qc], "ZZ", Alice)
		#	m2 = parity_meas([qa, qc], "ZZ", Alice)
		
		if row == 0:
			m0,m1,m2 = measR0(qa,qc,Alice)
		
		'''
		if row == 0:
			m0 = parity_meas([qa, qc], "XI", Alice)
			m1 = parity_meas([qa, qc], "XX", Alice)
			m2 = parity_meas([qa, qc], "IX", Alice)
		elif row == 1:
			m0 = parity_meas([qa, qc], "XZ", Alice, negative=True)
			m1 = parity_meas([qa, qc], "YY", Alice)
			m2 = parity_meas([qa, qc], "ZX", Alice, negative=True)
		elif row == 2:
			m0 = parity_meas([qa, qc], "IX", Alice)
			m1 = parity_meas([qa, qc], "ZZ", Alice)
			m2 = parity_meas([qa, qc], "ZI", Alice)'''
		
		
		print("Alice's results for row ",row," are ",m0," ",m1," ",m2)
		
		
		'''print("\n")
		print("==========================")
		print("App {}: row is:".format(Alice.name))
		for _ in range(row):
			print("(___)")
		print("({}{}{})".format(m0, m1, m2))
		for _ in range(2-row):
			print("(___)")
		print("==========================")
		print("\n")'''

		# Clear qubits
		qa.measure()
		qc.measure()



