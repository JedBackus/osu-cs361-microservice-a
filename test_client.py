import zmq

context =zmq.Context()

print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5678")

socket.send_string("start")
message = socket.recv()
print(message)


request = input("Enter some words: ")
socket.send_string(request)

message = socket.recv()
message = message.decode('ASCII')
message = float(message)

print(f"Calculated WPM: [ {message} ]")

