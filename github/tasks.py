__author__ = 'prism'
import json
import requests
from datetime import datetime
import pytz
from django.utils import timezone
# from celery import shared_task
#
#
# @shared_task
# def nisha():
#     print('x' + 'hi')
#     open('test.txt', 'a').close()


def get_data():
    url = 'https://api.github.com/users/pyprism/events?per_page=100'
    headers = {'Authorization': 'token 9f9b2f31ce0fc1784381202517ce4732536178f8', 'Time-Zone': 'Asia/Dhaka'}
    raw_response = requests.get(url, headers=headers)
    response = raw_response.json()
    for i in response:
        if 'PushEvent' == i['type']:
            data = i['created_at']
            print(data[:10] == datetime.now(pytz.timezone('Asia/Dhaka')).strftime("%Y-%m-%d"))
            #print(data[:10])
            #print(datetime.now(pytz.timezone('Asia/Dhaka')).strftime("%y-%m-%d"))
    return response
    #return datetime.now(pytz.timezone('Asia/Dhaka')).strftime("%d/%m/%y")

# get_data()
