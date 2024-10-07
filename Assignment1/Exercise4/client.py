import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 8080)) 
        print("Enter a message to send to the server (type 'exit' to quit): ")

        while True:
            message = input("*******Input*******\n")
            s.sendall(message.encode())

            if message.lower().strip() == "end":
                print("end connection with server")
                break

            data = s.recv(100)
            print(f"Server reply:\n {data.decode()}")

if __name__ == "__main__":
    main()
