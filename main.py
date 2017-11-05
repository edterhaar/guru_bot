from guru_bot import AskGuru
from irc import IRC, MessageTypes
import sys
import argparse

def main(channelName, serverName):
    channel = channelName if channelName.startswith('#') else '#' + channelName
    server = serverName
    nickname = "guru_bot"

    irc = IRC()
    irc.connect(server, channel, nickname)

    while 1:
        messageObj = irc.get_text()
        print(messageObj.all)

        if messageObj.type == MessageTypes.MESSAGE and messageObj.message.startswith(nickname):
            message = messageObj.message
            answer = AskGuru(message[message.find(nickname) + len(nickname):])
            for line in answer.split('\n'):
                irc.send(channel, line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Connects guru_bot to irc server and channel')
    parser.add_argument(
        '--channel',
        default="#eds_test_bed",
        help="Name of the chanel to connect to eg: 'general'")
    parser.add_argument(
        '--server',
        default="irc.freenode.net",
        help='Name of the server to connect to eg: irc.freenode.net')
    args = parser.parse_args()
    main(args.channel, args.server)
