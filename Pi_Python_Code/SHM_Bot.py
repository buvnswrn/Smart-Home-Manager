import os
import time
import re
from slackclient import SlackClient
#import pathlib
import Notify
import imagebot as imgbot
import db
slack_client =SlackClient('xoxb-305601000482-EagaR9CZuvKS2IxdMvteXxUW')
bot_id =None
botchannel='C8ZHL73RS'
t_end = time.time() + 60 * 5
response_text=None
RTM_DELAY=1
CMD="do"
REGEX= "^<@(|[WU].+)>(.*)"



def parse_bot_cmd(events):
    for event in events:
        if event["type"] == "message" and not "subtype" in event:
            id,msg=direct_mention(event["text"])
            print(event["text"])
            print(event["channel"])
            print(id,bot_id)
            if id == bot_id:
                return msg,event["channel"]
    return None,None

def direct_mention(msg):
    print("Checking for Direct mention")
    matches=re.search(REGEX,msg)
    return (matches.group(1),matches.group(2).strip()) if matches else (None,None)

def handle_cmd(cmd,channel):
    global slack_client
    print("Handling Command")
    default_msg="Response is Not Valid.Please enter a valid response.Enter*{}*.".format(response_text)

    response=None
    
    if cmd.lower()=="yes":
        print("User Responded Yes")
        response="OK.I will turn on the Guest mode for them."
        db.fetch("Guest",None)
    elif cmd.lower()=="no":
        print("User Responded No")
        response="OK.I will inform the Neighbors."
        Notify.notify_neighbor("Bhuvaneshwaran")
    
    slack_client.api_call(
        "chat.postMessage",
        channel=botchannel,
        text=response or default_msg
    )
    print("Handling Complete")

def notify(img):
    global botchannel
    global bot_id
    global slack_client
    global RTM_DELAY
    print("Informing User, Initialising Bot....")
    print("Bot Initialised")
    slack_client.api_call(
        "chat.postMessage",
            channel=botchannel,
            text="Hi, Did you send any Guest to your home?.(Yes/No).Please respond immedialtely within 5 min."
    )
    imgbot.sendimage(img)
    if slack_client.rtm_connect(with_team_state=False):
        sent_status="False"
        bot_id=slack_client.api_call("auth.test")["user_id"]
        while time.time() < t_end:
            cmd,botchannel=parse_bot_cmd(slack_client.rtm_read())
            print(cmd,botchannel)
            if cmd:
                print("in cmd")
                sent_status="True"
                handle_cmd(cmd,botchannel)
                break
            time.sleep(RTM_DELAY)
        if sent_status=="False":
            print("informing neighbors")
            Notify.notify_neighbor("Bhuvaneshwaran")
            slack_client.api_call("chat.postMessage",channel=botchannel,text="Didn't get a Response,Informing Neighbors")
    else:
        print("Connection failed.Exception traceback printed above.")


