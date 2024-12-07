import os
import requests

def check_for_updates(current_version):
    response = requests.get("https://example.com/latest-version")
    latest_version = response.text.strip()

    if latest_version != current_version:
        print(f"New version available: {latest_version}. Please update!")
    else:
        print("You are using the latest version.")
