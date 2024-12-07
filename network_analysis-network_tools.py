import pyshark

def analyze_netflow_data(file_path):
    cap = pyshark.FileCapture(file_path)
    for packet in cap:
        print(packet)
