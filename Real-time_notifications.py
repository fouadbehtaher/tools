import slack_sdk

def send_slack_notification(message):
    client = slack_sdk.WebClient(token='your-slack-token')
    client.chat_postMessage(channel='#general', text=message)
