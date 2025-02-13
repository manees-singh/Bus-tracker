import os
from dotenv import load_dotenv

from twilio.rest import Client


load_dotenv()
auth_token = os.getenv("AUTH_TOKEN")
account_sid = os.getenv("ACCOUNT_SID")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
to_phone_number = os.getenv("TO_PHONE_NUMBER")



class TwilioCall:
    def __init__(self, account_sid, auth_token, twilio_phone_number):
        
        self.client = Client(account_sid, auth_token)
        self.twilio_phone_number = twilio_phone_number


    def make_message(self, account_sid, auth_token, twilio_phone_number):
        message= self.client.messages.create(
            body= "Bus is arriving",
            from_= "+18337729101",
            to = "7854242973",
        )
        return message.sid

    def make_call(self, to_phone_number, message= "Hello! This is an automated call from Twilio."):
        
        call = self.client.calls.create(
            to=to_phone_number,
            from_=self.twilio_phone_number,
        
        )

        print(f"Call initiated! Call SID: {call.sid}")
        return call.sid  

        