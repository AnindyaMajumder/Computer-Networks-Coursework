import socket
import threading

data = 16
port = 5050
device_name = socket.gethostname() # user
server_ip = socket.gethostbyname(device_name) # 10.2.0.2
socket_addr = (server_ip, port)
client_count = 0

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(socket_addr)

server.listen()
print("Server listening .....")

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

def client_handle(server_socket, client_addr, client_count):
    connected = True
    while connected:
        client_msg_len = server_socket.recv(data).decode('utf-8')
        # print("Server ## Client message length is ", client_msg_len)
        
        if client_msg_len:
            client_msg = server_socket.recv(int(client_msg_len)).decode('utf-8')
            print(f"Received client{client_count} message:{client_msg}")
            
            if client_msg == "disconnect":
                print("Server is disconnected with -> ", client_addr)
                connected = False
            else:
                no_of_vowels = vowel_count(client_msg)
                server_socket.send(no_of_vowels.encode('utf-8'))
                
    server_socket.close()

while True:
    server_socket, client_addr = server.accept()
    print("Server is connected to -> ", client_addr)
    client_count += 1
    
    thread = threading.Thread(target=client_handle, args=(server_socket, client_addr, client_count))
    thread.start()