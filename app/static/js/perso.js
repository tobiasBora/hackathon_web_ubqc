/* Important Note:

   We need to make requests to the server. It is considered bad
   practice [1] to send synchronous requests in Javascript because it
   basically locks the browser... So it means that all requests needs
   to be done asynchonously, with what is so called "promises". If
   you are interested on how promises work in javascript, feel free
   to read [2]. However, here is a small rule of thumb:

   
   - When you want to create a function, use the 'async' keyword
   before the "function" keyword, that means 'the function may
   need some asynchronous calls, and is therefore asynchronous':

   ```
   async function myfunction() {
     return "Bob"
   }
   ```
   
   - When you call an asynchronous function inside an (asynchronous)
   function, use the 'await' key word right after the equal sign:

   ```
   async function my_dummy_function() {
     const myvalue = await myfunction()
     alert(myvalue)
   }
   ```

   If you don't need to get the result of the function, and just
   want to run it (asynchronously), it's easy, just write the name as usual!

   ```
   my_dummy_function()
   ```

   That's all! Just one thing however: it's not possible to use
   'await' in "top level", i.e. you must always use await inside a
   function. It makes sure that if you load a module, it does not
   "block". So if you want to use it in the top level code, just
   create a dummy function (like I did above), and call the function in the top level !

   PS: For people familiar with callbacks/promises, you can also use
   the '.then()' syntax that will basically take the result of the
   first function, and pass it the the next function. It's just a
   matter of preference! So for example, instead of creating this
   dummy function, you could have done:
   
   ```
   myfunction().then(
     function(name) {
       alert(name)
     }
   )
   ```

   Or, for people that like the arrow function syntax: () => { }:
   ```
   myfunction().then( (name) => {alert(name)} )
   ```

   PPS: It's not about programming, but if you want to debug and see
   what JSON file is sent/received from the server, there is a
   great function in firefox/chromium called: just press "F12"
   (firefox) to open development console, and then go to the Tab
   "Network". Refresh the page: you will see all files that are
   loaded by firefox, including the javascript calls to the server.
   To filter JSON files, you can even click on "XHR" on the top menu.
   Then, just click on the JSON request, and on the right tab you
   will get the Headers (useful to check that status code is 200/201)
   , Param (what the javascript sent), and Response (what the server
   responded). Nice to use to check if the error is client-side or
   server-side!
   
   
   [1] https://stackoverflow.com/questions/2246661/ajax-without-a-callback
   [2] https://medium.com/@bluepnume/learn-about-promises-before-you-start-using-async-await-eb148164a9c8

 */

async function fetchPost(url, data) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    // body data type must match "Content-Type" header
    body: JSON.stringify(data)
  });
  // parses JSON response into native JavaScript objects
  return await response.json(); 
}

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
        // List of entanglements [(id1, id2), (id2, id4),...]
        this.cz = []
        this.flow = {}
        // dict of id -> measurement 0/1
        this.measurements = {}
    }

    // Step 1: send qubits
    async send_plus_theta(id, theta_int) {
        // Will create the state on the server
        // Address: /preparationQubit
        // {
        //     'id': (0,0),
        //     'theta': 4
        // }
        // Return:
        // {'error': False}
        const data = await fetchPost('/preparationQubit',
                                     {
                                         id: id,
                                         theta: theta_int
                                     }
        )
        this.random_thetas[id] = theta_int
        // Here, you can access the data using for example
        // data.error, or data['error']:
        if (('error' in data) && (!data.error)) {
            // alert("There is no error :D")
            return true
        } else {
            // alert("There is an error :(")
            return false
        }
    }

    async get_random_theta(id) {
        return this.random_thetas[id]
    }
    
    // Step 2: create graph
    async send_CZ_list(id_pair_list) {
        // Id_coupld is a list of couple [(id1, id2), (id2, id3),...]
        // that represents the graph to send.
        // TODO: send that to server
        // Address: /preparationGraphState
        // {
        //    'entanglement_list': [
        //        ( (0,0) , (1,0) ),
        //        ( (1,1) , (1,1) ),
        //        ( (0,2) , (1,2) ),
        //    ]
        // }
        // Return:
        // {'error': False}
        this.cz.concat(id_pair_list)
        return true
    }

    // Generate the flow (once is enough)
    async generate_flow() {
        // TODO: compute the flow
        return self.flow
    }

    // Return the flow without recomputing it
    async get_flow() {
        return self.flow
    }

    // Step 3: compute recommended angles
    async get_recommended_angles(id, theta_int) {
        angle = 0
        // TODO compute the recommenced angle from the flow
        return angle
    }

    // Step 4: send angle to server
    async send_measurement_angle(id, phi, r) {
        // TODO: send to server
        // Address: /measurementAngle
        // {
        //    'id': (0,0),
        //    'theta': 4
        // }
        // Return measurement:
        // {'measurement': 0}
        // Returns the measurement sent by the server,
        // and the corrected measurement with r
        return (0, 1)
    }
}

alert("Javascript loaded, let's start UBQC and send one qubit!")
// Entry point of the page
async function start_ubqc() {
    let ubqc = new UBQC()
    // Just for demo, notice the "await" keyword!
    const result = await ubqc.send_plus_theta((0,0), 4)
    if (result) {
        alert("There is no error :D")
    } else {
        alert("There is an error :(")
    }
    alert("Thanks for playing with my game !")
}

start_ubqc()
