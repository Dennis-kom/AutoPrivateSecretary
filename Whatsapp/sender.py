import pywhatkit
import datetime

class WhatsappSender:

    def __init__(self, destination_phone_number, message):
        self.dest_number = destination_phone_number
        self.message: str = message


    def send(self):

        pywhatkit.sendwhatmsg("", "מתי את רוצה שאני אקח אותכן בערך?", 18, 42)
