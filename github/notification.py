__author__ = 'prism'
from twilio.rest import TwilioRestClient
from django.conf import settings


def twilio():
    """
    Send SMS
    """
    account_sid = settings.JSON_DATA['account_sid']
    auth_token = settings.JSON_DATA['auth_token']
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(body="Commit early, commit often. A tip for version"
                                          " controlling- not for relationships",
                                     to=settings.JSON_DATA['to'], from_=settings.JSON_DATA['from'])
