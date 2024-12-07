import os
import requests

def check_for_updates(current_version):
    response = requests.get("https://api.example.com/check_for_updates")
    latest_version = response.json()['latest_version']
    
    if current_version < latest_version:
        print(f"New update available: {latest_version}")
        return True
    return False

def notify_user_about_update():
    if check_for_updates("1.0.0"):
        print("A new update is available. Please update the tool to the latest version.")
    else:
        print("You are using the latest version.")
