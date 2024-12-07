import subprocess

def run_snort_for_ids():
    result = subprocess.run(['snort', '-A', 'console', '-c', '/etc/snort/snort.conf', '-i', 'eth0'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def detect_ddos_attack(network_data):
    threshold = 10000  # حد للحركة غير الطبيعية
    total_traffic = sum([flow['bytes_sent'] + flow['bytes_received'] for flow in network_data])
    if total_traffic > threshold:
        return "Potential DDoS Attack Detected"
    else:
        return "Normal Traffic"
