import ssl
import socket

def create_ssl_server(host, port, certfile, keyfile):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    
    print(f"SSL server started on {host}:{port}")
    
    while True:
        client_socket, client_address = server.accept()
        ssl_socket = context.wrap_socket(client_socket, server_side=True)
        print(f"Connection established with {client_address}")
        ssl_socket.send(b"Hello, secure world!")
        ssl_socket.close()

def create_ssl_client(host, port, certfile):
    context = ssl.create_default_context()
    context.load_verify_locations(certfile)
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_client = context.wrap_socket(client, server_hostname=host)
    ssl_client.connect((host, port))
    
    print(f"Connected to {host}:{port}")
    data = ssl_client.recv(1024)
    print(f"Received: {data.decode()}")
    ssl_client.close()
