import socket

def main():
    host = '127.0.0.1'  
    port = 8080  

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))  
        print(f"Connected to server at {host}:{port}")
        print("Enter a message to send to the server (type 'exit' to quit): ")

        while True:
            message = input("*******Input*******\n")
            s.sendall(message.encode())

            if message.lower().strip() == "exit":
                print("exit íconnection with server")
                break

            data = s.recv(100)
            print(f"Server reply:\n {data.decode()}")

if __name__ == "__main__":
    main()
