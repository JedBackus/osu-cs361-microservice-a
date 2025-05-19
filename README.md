# osu-cs361-microservice-a


Word-Per-Minute (WPM) Calculator:

This WPM calculator is designed to run on a local host, by default on port 5678 (although this could be easily adjusted to fit the needs of the user).

The program uses the zmq (ZeroMQ) python package to open a TCP socket as a server. ( Server uses REP, client should use REQ )

    Server:
      context = zmq.Context()
      socket = context.socket(zmq.REP)
      socket.bind("tcp://*:5678")

To use the program, ensure the client socket connects on the same port, and when ready to begin calculating WPM send a message to the program containing the string "start" ( using socket.send_string() ). 

    Client: 
      context =zmq.Context()
      socket = context.socket(zmq.REQ)
      socket.connect("tcp://localhost:5678")
    
      socket.send_string("start")

Provided the message was received correctly, the server will respond with "wpm calc started.." and the client must listen for this message before continuing ( using socket.recv() ). 

    Client: 
      socket.recv()
      
    Server: 
      socket.send_string("wpm calc started..")

Once the confirmation has been received, the server will start a timer and await the user input. 

The client should then take the words typed by the user and pass them to the server as a string.

    Client: 
      socket.send_string(user_input)

The server will accept the string, split it into words, and run the calculations to determine the user's WPM. It will then pass the result back to the client as a string.

    Server: 
      socket.send_string(wpm)

    Client:
      socket.recv()
    
In summary, the client connects to the server on localhost:5678, passes "start", receives "wpm calc started..", passes user input, receives WPM.

NOTES: 

  Client may need to use received_message.decode() to convert received message to string (may not be necessary, but good to know if needed)

  If the program initially receives anything other than "start" it will respond with a message that tells the client to send "start" to use the WPM calculator. (this is the extent of the error handling the program does, however it should be sufficient for most cases)
  
  Program calculates Gross WPM. Meaning that it does not account for misspelled words, or other mistakes. 


UML Diagram: 

![Slide1 3](https://github.com/user-attachments/assets/1c045a61-213c-474a-9c00-1f7b623bc7c0)

