import socket
from sys import argv
import message_pb2


def main():
    host = None
    port = None
    try:
        if len(argv) > 2:
            host = argv[1]
            port = int(argv[2])
        elif len(argv) > 1:
            port = int(argv[1])
        else:
            raise ValueError
    except:
        host = host or "127.0.0.1"
        port = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to the server")
        # Exercise 3
        handshake_data = s.recv(1024)
        handshake = message_pb2.HandshakeMessage()
        handshake.ParseFromString(handshake_data)
        if handshake.error:
            print("Handshake failed, closing connection.")
            return
        else:
            print(f"Handshake successful, assigned ID: {handshake.id}")

        while True:
            try:
                data = input("Enter a message: ")
            except:
                data = "end"
            if data == "end":
                s.sendall(data.encode())
                break
            #Exercise 2&3
            message = message_pb2.NormalMessage()
            message.from_ = handshake.id 
            message.to = 0  
            message.msg = data
        
            s.sendall(message.SerializeToString())
            print("Message sent")

            response_raw = s.recv(1024)
            response = message_pb2.NormalMessage()
            response.ParseFromString(response_raw)
            print(f"Received from {response.from_} to {response.to}: {response.msg}")
            
        print("Closing connection")


if __name__ == "__main__":
    main()
