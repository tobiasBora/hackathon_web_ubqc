import os
from flask import Flask, render_template, request, session, g, redirect
from contextlib import ExitStack
from ubqc import app

from pathlib import Path
from cqc.pythonLib import CQCConnection, qubit

@app.route('/')
@app.route('/index')
def index():
    return render_template('accueil.html', titre='Accueil')
