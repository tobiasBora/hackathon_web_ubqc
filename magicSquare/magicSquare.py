#!/usr/bin/env python3
import random
import string
# Useful to avoid having "with ..." everywhere.
from contextlib import ExitStack
# Quantum library
from cqc.pythonLib import CQCConnection

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
        self.alice_name = "Alice_{}".format(self.session_id)
        self.bob_name = "Bob_{}".format(self.session_id)
        # Debug: it works
        # self.alice_name = "Alice"
        # self.bob_name = "Bob"
        # Create the contexts to connect to CQC
        self.cqc_alice = self.global_stack.enter_context(
            CQCConnection(self.alice_name)
        )
        self.cqc_bob = self.global_stack.enter_context(
            CQCConnection(self.bob_name)
        )
        # Create two EPR pairs
        self.log("Will generate EPR pairs...")
        self.q1_a = self.cqc_alice.createEPR(self.bob_name)
        self.log("Alice sent the first EPR pair...")
        self.q1_b = self.cqc_bob.recvEPR()
        self.log("Bob received the first EPR pair...")
        self.q2_a = self.cqc_alice.createEPR(self.bob_name)
        self.log("Alice sent the second EPR pair...")
        self.q2_b = self.cqc_bob.recvEPR()
        self.log("Bob received the second EPR pair...")

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

def main():
    with ExitStack() as global_stack:
        magic_square = MagicSquare(global_stack)
        magic_square.print_info()
        ma = magic_square.alice_measurement(0)
        mb = magic_square.bob_measurement(0)
        print("Alice: {}".format(ma))
        print("Bob: {}".format(mb))
        if ma == mb:
            print("They have the same result :D")
        else:
            print("Grr...! They have different result :-(")

if __name__ == '__main__':
    main()
