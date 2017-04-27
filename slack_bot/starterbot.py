import os
import time
import requests
from slackclient import SlackClient
from parsing_incoming import parse_inbound
from space_conversion import convert_spaces

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    message = parse_inbound(command)
    ready_message = convert_spaces(message)
    if len(ready_message) < 3:
        for i in range(3 - len(ready_message)):
            ready_message.append("")
    meme_url = "http://apimeme.com/meme?meme={}&top={}&bottom={}".format(
        ready_message[0], ready_message[1], ready_message[2])
    r = requests.get(meme_url)
    if 'No meme found' not in r.text:
        response = meme_url
    else:
        response = "https://img.memesuper.com/abd9230cf6066288b1ddce774a9baeee_do-you-even-meme-do-u-even-meme_400-400.jpeg"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
