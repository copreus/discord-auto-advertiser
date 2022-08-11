import httpx, time
#Put your discord token in the brackets
token = ""

#Put what message you want sent in the brackets below
content = "Hello"

#This is where the message will be sent to. To get a channel ID, search youtube or google.
channelid = ""

#Delay before sending message again in SECONDS
delay = 3

while True:
    time.sleep(delay)
    ree = httpx.post(f'https://discord.com/api/v9/channels/{channelid}/messages', headers={'authorization': token}, json={"content": content})
    if ree.status_code == 200:
        print(f"Sent {content} to channel with ID {channelid}")
    else:
        print("Failed to send message! Invalid token perhaps?")
        time.sleep(15)
