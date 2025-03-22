import socket

data = 16
format = "utf-8"
port = 5050
device_name = socket.gethostname()
client_ip = socket.gethostbyname(device_name)
socket_addr = (client_ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(socket_addr)

def send_msg(msg):
    msg_body = msg.encode(format)
    msg_len = len(msg_body)
    msg_len_enc = str(msg_len).encode(format)
    msg_len_enc = msg_len_enc + b" " * (data-len(msg_len_enc))
    
    client.send(msg_len_enc)
    client.send(msg_body)
    
    server_response = client.recv(128).decode(format)
    print("Server respond: ", server_response)
    
send_msg(f"Client's device name {device_name}\nClient's ip address {client_ip}")
send_msg("disconnect")