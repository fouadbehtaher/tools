from pyshark import FileCapture

def analyze_netflow_data(file_path):
    cap = FileCapture(file_path)
    for packet in cap:
        print(packet)
