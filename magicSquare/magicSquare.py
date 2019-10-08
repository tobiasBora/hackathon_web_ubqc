#!/usr/bin/env python3
import random
import string
import time
# Useful to avoid having "with ..." everywhere.
from contextlib import ExitStack
# Quantum library
from cqc.pythonLib import CQCConnection
# Create new network
# https://softwarequtech.github.io/SimulaQron/html/ConfNodes.html
from simulaqron.network import Network

def id_generator(size=10, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

class MagicSquare:
    def __init__(self, global_stack, session_id=None, debug=False):
        self.global_stack = global_stack
        self.debug = debug
        if session_id:
            self.session_id = str(session_id)
        else:
            self.session_id = id_generator()
        ## Name of parties
        self.alice_name = "Alice"
        self.bob_name = "Bob"
        
        ## Create a new network
        self.network_name = self.session_id
        print("Creation of network")
        self.log("Creation of network {}".format(self.network_name))
        nodes = [self.alice_name, self.bob_name]
        topology = {
            self.alice_name: [self.bob_name],
            self.bob_name:   [self.bob_name]
        }
        self.network = Network(name=self.network_name,
                               nodes=nodes,
                               topology=topology,
                               force=True,
                               new=True)
        self.network.start()
        self.log("Network started!")
        time.sleep(5)
        ## Create the contexts to connect to CQC
        self.cqc_alice = self.global_stack.enter_context(
            CQCConnection(self.alice_name,
                          network_name=self.network_name,
                          conn_retry_time=1)
        )
        time.sleep(3)
        self.log("Alice CQC connection done!")
        self.cqc_bob = self.global_stack.enter_context(
            CQCConnection(self.bob_name,
                          network_name=self.network_name,
                          conn_retry_time=1)
        )
        time.sleep(3)
        self.log("Bob CQC connection done!")
        # Create two EPR pairs
        self.log("Will generate EPR pairs...")
        self.q1_a = self.cqc_alice.createEPR(self.bob_name)
        self.log("Alice sent the first EPR pair...")
        time.sleep(3)
        self.q1_b = self.cqc_bob.recvEPR()
        self.log("Bob received the first EPR pair...")
        time.sleep(1)
        self.q2_a = self.cqc_alice.createEPR(self.bob_name)
        self.log("Alice sent the second EPR pair...")
        time.sleep(1)
        self.q2_b = self.cqc_bob.recvEPR()
        self.log("Bob received the second EPR pair...")
        time.sleep(1)

    def log(self, message):
        if self.debug:
            print(message)

    def print_info(self):
        print("The session id is {}".format(self.session_id))
        
    def alice_measurement(self, row):
        self.log("Alice will measure...")
        m0 = self.q1_a.measure()
        self.log("Alice measured {}.".format(m0))
        return m0

    def bob_measurement(self, column):
        self.log("Bob will measure...")
        m0 = self.q1_b.measure()
        self.log("Bob measured {}.".format(m0))
        return m0


def parallel_epr():
    with ExitStack() as global_stack:
        magic_square = MagicSquare(global_stack, debug=True)
        magic_square.print_info()
        magic_square2 = MagicSquare(global_stack, debug=True)
        magic_square2.print_info()
        ma = magic_square.alice_measurement(0)
        mb = magic_square.bob_measurement(0)
        ma2 = magic_square2.alice_measurement(0)
        mb2 = magic_square2.bob_measurement(0)
        print("Alice: {}".format(ma))
        print("Bob: {}".format(mb))
        print("Alice 2: {}".format(ma2))
        print("Bob 2: {}".format(mb2))
        if ma == mb:
            print("They have the same result :D")
        else:
            print("Grr...! They have different result :-(")
        if ma2 == mb2:
            print("They have the same result :D")
        else:
            print("Grr...! They have different result :-(")
            
def one_exec():
    with ExitStack() as global_stack:
        magic_square = MagicSquare(global_stack, debug=True)
        magic_square.print_info()
        ma = magic_square.alice_measurement(0)
        mb = magic_square.bob_measurement(0)
        print("Alice: {}".format(ma))
        print("Bob: {}".format(mb))
        if ma == mb:
            print("They have the same result :D")
        else:
            print("Grr...! They have different result :-(")

def main():
    # Usually works, but sometimes times out without apparent reason:
    print("=== Let's try a single exec")
    one_exec()
    # print("=== Let's try another single exec")
    # one_exec()
    # Fails:
    print("=== Let's try two parallel exec")
    parallel_epr()
            
if __name__ == '__main__':
    main()
