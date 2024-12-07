import requests
import json

def check_for_update(current_version):
    update_url = "https://example.com/check_for_update"
    response = requests.get(update_url, params={"version": current_version})
    update_info = response.json()
    return update_info

def notify_user_of_update(update_info):
    print(f"New version available: {update_info['new_version']}")
    print(f"Release Notes: {update_info['release_notes']}")
