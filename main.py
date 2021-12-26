from slack_sdk import WebClient

TOKEN = "" # User or bot token
CHANNEL = "" # Channel of the message
TIMESTAMP = "" # Timestamp of the message

client = WebClient(token=TOKEN)

def getUsers(client, CHANNEL, TIMESTAMP):
    response = client.reactions_get(channel=CHANNEL, timestamp=TIMESTAMP, full=True)
    user_ids = response['message']['reactions'][0]['users']
    return user_ids

def getName(user_id):
    # Call the users.info method using the WebClient
    result = client.users_info(user=user_id)
    # Parse Slack user's display name
    name = result['user']['profile']['display_name']
    return name

user_ids = getUsers(client, CHANNEL, TIMESTAMP)
names = []

for user_id in user_ids:
    name = getName(user_id)
    names.append(name)

print(names)
