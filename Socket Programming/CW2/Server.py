import socket

data = 16
port = 5050
device_name = socket.gethostname() 
server_ip = socket.gethostbyname(device_name) 
socket_addr = (server_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(socket_addr)

def vowel_count(msg):
    vowels = "aeiouAEIOU"
    count = 0
    
    for i in msg:
        if i in vowels:
            count += 1
    
    if count == 0:
        return "Not enough vowels"
    elif count <= 2:
        return "Enough vowels I guess"
    else:
        return "Too many vowels"

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
            print("Received client message: ", client_msg)
            
            if client_msg == "disconnect":
                print("Server is disconnected with -> ", client_addr)
                connected = False
            else:
                no_of_vowels = vowel_count(client_msg)
                server_socket.send(no_of_vowels.encode('utf-8'))
                
    server_socket.close()