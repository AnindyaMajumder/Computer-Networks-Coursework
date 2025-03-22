import socket

data = 16
port = 5050
device_name = socket.gethostname() # user
server_ip = socket.gethostbyname(device_name) # 10.2.0.2
socket_addr = (server_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(socket_addr)

server.listen()
print("Server listening .....")

while True:
    server_socket, client_addr = server.accept()
    print("Server is connected to -> ", client_addr)
    
    connected = True
    while connected:
        client_msg_len = server_socket.recv(data).decode('utf-8')
        # print("Server ## Client message length is ", client_msg_len)
        
        if client_msg_len:
            client_msg = server_socket.recv(int(client_msg_len)).decode('utf-8')
            
            if client_msg == "disconnect":
                print("Server is disconnected with -> ", client_addr)
                connected = False
            else:
                print("Server ## Client's message: ", client_msg)
            
            server_socket.send("Message Received".encode('utf-8'))
                
    server_socket.close()