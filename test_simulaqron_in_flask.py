# 1. start simulaqron
# 2. type: FLASK_APP=test_simulaqron_in_flask.py flask run 
# 3. send POST resquest to /test with json body  {"basis": "X"} or {"basis":"Z"}
# Z should output always 0. X outputs a random bit

from flask import Flask 
from flask import request
from pathlib import Path

from cqc.pythonLib import CQCConnection, qubit

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
     return "Hello world"

@app.route("/test", methods=["POST"])
def measure():
     print("Entering test")
     basis = request.json.get("basis")
     
     with CQCConnection("Alice") as Alice:
          print("Connected to Alice")
          q = qubit(Alice)
          if basis == "X":
               q.H()
          o = q.measure()
          print("Done measuring: ", o)
               
     return str(o)
