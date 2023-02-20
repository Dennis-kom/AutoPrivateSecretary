import pywhatkit
import datetime
import requests
import http.client
class WhatsappSender:

    def __init__(self, destination_phone_number, message):
        self.dest_number = destination_phone_number
        self.message: str = message


    def send(self):

        pywhatkit.sendwhatmsg("+972544900054", "test", 0, 12)


