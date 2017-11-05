'''
Module to inteact with IRC
'''

import socket
from time import sleep
from enum import Enum

class MessageTypes(Enum):
    UNKNOWN = 0
    PING = 1
    MESSAGE = 2

class MessageObject:
    def __init__(self, text):
        self.all = text

        if "PING" in text:
            self.type = MessageTypes.PING
        elif "PRIVMSG" in text:
            self.type = MessageTypes.MESSAGE
            indexOfSecondColon = text.find(":", text.find(":") + 1)
            self.header = text[: indexOfSecondColon]
            self.message = text[indexOfSecondColon + 1:]
        else:
            self.type = MessageTypes.UNKNOWN

class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(("PRIVMSG " + chan + " :" + msg + "\r\n").encode('UTF-8'))

    def connect(self, server, channel, botnick):
        # defines the socket
        print("connecting to:" + server)
        self.irc.connect((server, 6667))
        self.irc.send(bytes("USER " + botnick + " " +
                            botnick + " " + botnick + ": guru_bot rules\r\n", 'UTF-8'))
        sleep(0.1)
        self.irc.send(("NICK " + botnick + "\r\n").encode('UTF-8'))
        sleep(0.2)
        self.irc.send(("JOIN " + channel + "\r\n").encode('UTF-8'))

    def is_message(self, text):
        return text.startwith("PRIVMSG")

    def get_text(self):
        text = self.irc.recv(4096).decode('utf-8')
        messageObject = MessageObject(text)

        if messageObject.type == MessageTypes.PING:
            self.irc.send(str('PONG ' + text.split(':')[1] + '\r\n').encode('UTF-8'))

        return messageObject
