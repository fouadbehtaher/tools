import ssl
import socket

def create_secure_context():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.options |= ssl.OP_NO_SSLv2
    context.options |= ssl.OP_NO_SSLv3
    context.options |= ssl.OP_NO_TLSv1
    context.options |= ssl.OP_NO_TLSv1_1
    context.set_ciphers('ECDHE-ECDSA-AES128-GCM-SHA256')
    
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    context.load_verify_locations(cafile="ca-cert.pem")
    context.verify_mode = ssl.CERT_REQUIRED
    return context

def secure_connection():
    try:
        context = create_secure_context()
        with socket.create_connection(('localhost', 443)) as sock:
            with context.wrap_socket(sock, server_hostname='localhost') as secure_sock:
                print("Secure connection established.")
    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except socket.error as e:
        print(f"Socket Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
