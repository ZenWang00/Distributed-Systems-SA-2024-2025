import socket
import threading
'''
Possible alternatives
1. use process for each client
e.g
from multiprocessing import Process
process = Process(target=client_connection, args=(connection,address))

2. use asyncio function
e.g
import asyncio
async def client_connection(connection,address):
    ...
async def main():
    server = await asyncio.start_server(client_connection, '127.0.0.1', 8080)
    async with server:
        await server.serve_forever()
asyncio.run(main())
'''

def client_connection(connection,address):
    
    with connection:
         while True:
            data = connection.recv(100)
            message = data.decode().strip()

            print(f"*******connection by {address} *******")
            print(f"Message received: {message}")

            if message.strip().lower() == "end":
                print(f"Received 'end' command. Closing connection from {address} ")
                break
                
            reply = f"Server received: {message}"
            connection.sendall(reply.encode())

    print("Close connection with client")
    

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 8080))
        s.listen()
        print("Server is listening on port 8080...")
        
        while True:
            connection, address = s.accept()
            client_thread = threading.Thread(target=client_connection , args=(connection, address))
            client_thread.start()

if __name__ == "__main__":
    main()