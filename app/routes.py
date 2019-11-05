import os
import math
from flask import Flask, render_template, request, session, g, redirect
from contextlib import ExitStack
from ubqc import app

from pathlib import Path
from cqc.pythonLib import CQCConnection, qubit

@app.route('/')
@app.route('/index')
def index():
    return render_template('accueil.html', titre='Accueil')


global_stack = ExitStack()
serverState={}
Serveur=global_stack.enter_context( CQCconnection('Bob'))

@app.route('/preparationQubit', methods=['POST'])    
def preparationQubit():
	if not request.json or not 'theta' in request.json or not 'id' in request.json:
		abort(400)
		
	theta = request.json['theta']
	idi = request.json['id']
	
	qubit = qubit(Serveur)
	qubit = qubit.rot_Z(theta*(256/math.pi))
	serverState{idi}=qubit
	
	
	return jsonify({'error':False}), 201
	
	
@app.route('/preparationGraphState', methods=['POST'])    
def preparationGraphState():
	if not request.json or not 'entanglement_list' in request.json:
		abort(400)
	for ((x1,y1),(x2,y2)) in request.json['entanglement_list']:
		serverState((x1,y1)).CPHASE((x2,y2))
		
	return jsonify({'error':False}), 201
	
@app.route('/measurementAngle', methods=['POST'])    
def measureAngle():
	if not request.json or not 'theta' in request.json or not 'id' in request.json:
		abort(400)
		
	theta = request.json['theta']
	idi = request.json['id']
	
	serverState{idi}.ROT_Z(theta)
	s=serverState{idi}.measure()
	
	return jsonify({'measurement':s}), 201
