import os
from flask import Flask, render_template, request, session, g, redirect
from app import app
import sqlite3
from contextlib import ExitStack

from pathlib import Path
from cqc.pythonLib import CQCConnection, qubit
from libmagicsquare import MagicSquare


@app.route('/')
@app.route('/index')
def index():
    return render_template('accueil.html', titre='Accueil')


def waiting(idsess):
    conn = sqlite3.connect('sessions.db')
    curr=conn.cursor()
    items=curr.execute("SELECT * FROM session WHERE id=? ", (idsess,))
    return render_template('waiting.html', items=items.fetchall() )

@app.route('/player1')
def p1():
    return render_template('p1.html', titre='player 1')

@app.route('/waiting1',methods = ["POST"])
def waiting1():
    conn = sqlite3.connect('sessions.db')
    ids = request.form["numsess"]
    numline = request.form["numline"]
    x1 = request.form["select1"]
    x2 = request.form["select2"]
    x3 = request.form["select3"]
    x=x1+x2+x3
    p2c= 0
    p2x= 0
    curr=conn.cursor()
    curr.execute("INSERT INTO session (id,p1line,p1val,p2col,p2val) VALUES (?,?,?,?,?)",[ids,numline,x,p2c,p2x] )
    conn.commit()
    return waiting(ids)

@app.route('/player2')
def p2():
    return render_template('p2.html', titre='Player 2')

@app.route('/waiting2',methods = ["POST"])
def waiting2():
    conn = sqlite3.connect('sessions.db')
    ids = request.form["numsess"]
    numcol = request.form["numline"]
    x1 = request.form["select1"]
    x2 = request.form["select2"]
    x3 = request.form["select3"]
    # Classical
    x=x1+x2+x3
    curr=conn.cursor()
    curr.execute("UPDATE session SET p2col=?, p2val=? WHERE id=? ", (numcol, x, ids))
    conn.commit()
    return waiting(ids)


@app.route('/results/<ids>/',methods = ["GET"])
def results(ids):
    conn = sqlite3.connect('sessions.db')
    curr=conn.cursor()
    items=curr.execute("SELECT * FROM session WHERE id=? ", (ids,))
    items1=items.fetchone()
    numline=int(items1[1])-1
    numcol=int(items1[3])-1
    # Quantum
    with ExitStack() as global_stack:
        magic_square = MagicSquare(global_stack, debug=True)
        ma = magic_square.alice_measurement(numline)
        mb = magic_square.bob_measurement(numcol)   
        return render_template('resultats.html', items1=items1, ma=ma, mb=mb, titre="Résultats")


