from django.conf import settings

import twilio
import twilio.rest

# example to send a sms
#from ImmOrbit.twillo_utils import send_twilio_message
#sms = send_twilio_message('+15005550006', 'Hello Endpointer,')

def send_twilio_message(to_number, body):
    client = twilio.rest.TwilioRestClient(
        settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    return client.messages.create(
        body=body,
        to=to_number,
        from_=settings.TWILIO_PHONE_NUMBER
    )
