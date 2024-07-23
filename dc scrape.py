import requests
import json
import os

#input data
token = input("Token : ")
channel_id = input("Channel ID : ")

url_recive = f"https://discord.com/api/v9/channels/{channel_id}/messages"
headers = {"Authorization": f"{token}"}

#get messages
r = requests.get(url_recive, headers=headers)
if r.status_code == 200:
    jsonn = json.loads(r.text)
    
    #clear console
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Reverse the order of messages to display oldest to newest
    jsonn.reverse()
    
    #display Messages
    print("\nMessages:")
    for value in jsonn:
        content = value["content"]
        author = value["author"]["username"]
        print(f"{author}: {content}", "\n")
else:
    print(f"Failed to retrieve messages: {r.status_code}")
