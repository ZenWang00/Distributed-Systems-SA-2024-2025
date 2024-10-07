import socket
from sys import argv

def main():
    try:
        port = int(argv[1])
    except:
        port = 8080

    print(f"Server started on port {port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("0.0.0.0", port))
        s.listen(1)
        print("Waiting for a client...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(100)
                message = data.decode().strip()
                print(f"Message received: {message}")

                if message.strip().lower() == "exit":
                    print("Received 'exit' command. Closing connection.")
                    break
                
                reply = f"Server received: {message}"
                conn.sendall(reply.encode())

        print("Close connection with client")

if __name__ == "__main__":
    main()
