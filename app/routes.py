import os
import math
from flask import Flask, render_template, request, session, g, redirect, abort, jsonify
from contextlib import ExitStack
from ubqc import app
import sys
from simulaqron.network import Network

from pathlib import Path
from cqc.pythonLib import CQCConnection, qubit

@app.route('/')
@app.route('/index')
def index():
    # We reinitialize the server to make sure we don't run out of qubits
    # Setup the network
    nodes = ["Alice", "Bob"]
    topology = {"Alice": ["Bob"], "Bob": ["Alice"]}
    network = Network(name="default", nodes=nodes, topology=topology, force=True)
    # Start the network
    network.start()
    
    return render_template('accueil.html', titre='Accueil')


global_stack = ExitStack()
serverState={}
Serveur=global_stack.enter_context( CQCConnection('Bob'))

def log(msg):
    print(msg, file=sys.stdout, flush=True)

@app.route('/preparationQubit', methods=['POST'])    
def preparationQubit():
    global serverState
    global Serveur
    if not request.json or not 'theta' in request.json or not 'id' in request.json:
        abort(400)
        
    theta = request.json['theta']
    idi = tuple(request.json['id'])
    log("[preparationQubit] idi: {}".format(idi))
    q1 = qubit(Serveur)
    # theta * pi/4 = step * 2 pi / 256
    # => step = theta * 32
    # If you get error CQCUnsuppError("Sequence not supported")
    # Then configure projectq backend:
    # simulaqron set backend projectq
    # simulaqron stop
    # simulaqron start
    q1.rot_Z(step=int(theta*32) % 256)
    serverState[idi]=q1
        
    return jsonify({'error':False}), 201
    
    
@app.route('/preparationGraphState', methods=['POST'])    
def preparationGraphState():
    global serverState
    global Serveur
    if not request.json or not 'entanglement_list' in request.json:
        abort(400)
    for couple_id in request.json['entanglement_list']:
        id1 = tuple(couple_id[0])
        id2 = tuple(couple_id[1])
        log(serverState)
        ## Works, but useless
        serverState[id1].rot_Z(42)
        serverState[id2].rot_Z(42)
        ## Fails... but WHY?
        serverState[id1].CPHASE(serverState[id2])
        
    return jsonify({'error':False}), 201
    
@app.route('/measurementAngle', methods=['POST'])    
def measureAngle():
    global serverState
    global Serveur
    if not request.json or not 'theta' in request.json or not 'id' in request.json:
        abort(400)
        
    theta = request.json['theta']
    idi = tuple(request.json['id'])
    
    serverState[idi].ROT_Z(theta)
    s=serverState[idi].measure()
    
    return jsonify({'measurement':s}), 201
