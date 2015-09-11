__author__ = 'prism'
import requests
from hiren import json_data
# timezone specific request "Time-Zone: Europe/Amsterdam"
# optional header User-Agent: Awesome-Octocat-App
# url parameter for max item per page &per_page=100'
# scope repo:status
# login url : https://github.com/login/oauth/authorize?client_id=''&redirect_uri=''&scope=''&state='random string'


def auth():
    url = "https://github.com/login/oauth/authorize"
    client_id = json_data['client_id']
    redirect_uri = json_data['redirect_uri']
    scope = 'repo:status'
    return url + '?' + 'client_id=' + client_id + '&' + 'redirect_uri=' + redirect_uri + '&' + 'scope=' + scope
