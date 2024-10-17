import socket
from sys import argv
from threading import Thread, Lock
import message_pb2
import time

connected_users = 0
lock = Lock()

# Exercise 1
def server_count():
    global connected_users
    while True:
        command = input()
        if command == "num_users":
            with lock:
                print(f"Number of connected users: {connected_users}")
        time.sleep(0.1)

def handle_client(conn, addr):
    global connected_users
    with conn:
        with lock:
            connected_users += 1
        print(f"Connected by {addr}")
        # Exercise 3
        try:
            handshake = message_pb2.HandshakeMessage()
            handshake.id = int(time.time())
            handshake.error = False
            conn.sendall(handshake.SerializeToString())

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if data == b"exit":
                    break
                # Exercise 2
                message = message_pb2.NormalMessage()
                message.ParseFromString(data)
                print(f"Received from {message.from_} to {message.to}: {message.msg}")
                conn.sendall(data)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            with lock:
                connected_users -= 1
        print(f"Closing connection to {addr}")


def main():
    try:
        port = int(argv[1])
    except:
        port = 8080

    Thread(target=server_count, daemon=True).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", port))
        print(f"Server started on port {port}")
        print("Waiting for a client...")
        s.listen()
        while True:
            try:
                conn, addr = s.accept()
                Thread(target=handle_client, args=(conn, addr)).start()
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    main()
