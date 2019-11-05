class UBQC {
    constructor() {
        // - The ID of qubits will be couples of integer (int, int)
        // - The thetas_int are angles represented by multiple of
        //   pi/4.
        // - a flow is a dictionnary mapping ID to a couple of lists.
        //   The first list is the set D_x for correcting by an X.
        //   The second list is the set D_z for correcting by an Z.
        // - A measurement is either 0 or 1
        
        // dict of id -> random thetas
        this.random_thetas = {}
        this.cz = []
        this.flow = {}
        // dict of id -> measurement 0/1
        this.measurements = {}
    }

    // Step 1: send qubits
    send_plus_theta(id, theta_int) {
        // Will create the state on the server
        // TODO: send to server with json POST call
        // {
        //     'id': (0,0),
        //     'theta': 4
        // }
        this.random_thetas[id] = theta_int
        return true
    }

    // Step 2: create graph
    send_CZ_list(id_pair_list) {
        // Id_coupld is a list of couple [(id1, id2), (id2, id3),...]
        // that represents the graph to send.
        // TODO: send that to server
        // {
        //    'entanglement_list': [
        //        ( (0,0) , (1,0) ),
        //        ( (1,1) , (1,1) ),
        //        ( (0,2) , (1,2) ),
        //    ]
        // }
        this.cz.concat(id_pair_list)
        return true
    }

    // Generate the flow (once is enough)
    generate_flow() {
        // TODO: compute the flow
        return self.flow
    }

    // Return the flow without recomputing it
    get_flow() {
        return self.flow
    }

    // Step 3: compute recommended angles
    get_recommended_angles(id, theta_int) {
        angle = 0
        // TODO compute the recommenced angle from the flow
        return angle
    }

    // Step 4: send angle to server
    send_measurement_angle(id, theta_int) {
        // TODO: send to server
        // Return measurement
        return 0
    }
}
