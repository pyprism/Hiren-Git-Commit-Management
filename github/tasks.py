__author__ = 'prism'
import json
import requests
from datetime import datetime
from github.models import Hiren, Counter
import pytz
from github.notification import twilio
from celery import shared_task

@shared_task
def get_data():
    """
    Call github api, send sms, update commit activity to db
    """
    url = 'https://api.github.com/users/pyprism/events?per_page=100'
    nisha = Hiren.objects.get()
    headers = {'Authorization': 'token ' + nisha.access_token, 'Time-Zone': 'Asia/Dhaka'}
    raw_response = requests.get(url, headers=headers)
    response = raw_response.json()
    committed_sin = 0  # total commit  :D
    for i in response:
        if 'PushEvent' == i['type']:
            data = i['created_at']
            if data[:10] == datetime.now(pytz.timezone('Asia/Dhaka')).strftime("%Y-%m-%d"):
                committed_sin = committed_sin + 1
            if committed_sin:  # if there is no commit
                twilio()
    obj = Counter(number=committed_sin)
    obj.save()

