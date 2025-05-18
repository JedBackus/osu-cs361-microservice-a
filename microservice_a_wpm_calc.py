import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5678")

while True:

    message = socket.recv()
    if message.decode() == 'start':
        socket.send_string("wpm calc started..")
        start = time.time()
        print(start)
        message = socket.recv()
        end = time.time()

        message = message.decode('ASCII')
        words = len(message.split())

        print(len(message.split()))

        time_taken = (end - start) / 60
        wpm = words / time_taken
        wpm = str(round(wpm, 2))

        socket.send_string(wpm)
    else:
        socket.send_string("Please pass 'start' to initiate the WPM calculator...")


