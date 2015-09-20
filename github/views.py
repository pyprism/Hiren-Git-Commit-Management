from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from github.models import Hiren
import requests
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/hiren')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect(request.path)
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required
def hiren(request):
    """
    generate authorization  button and show revoke button
    """
    url = "https://github.com/login/oauth/authorize"
    client_id = settings.JSON_DATA['client_id']
    redirect_uri = settings.JSON_DATA['redirect_uri']
    scope = 'repo:status'
    login_btn = url + '?' + 'client_id=' + client_id + '&' + 'redirect_uri=' + redirect_uri + '&' + 'scope=' + scope
    try:
        nisha = Hiren.objects.get()
    except Hiren.DoesNotExist:
        return render(request, 'hiren.html', {'btn': login_btn, 'auth_button': False})
    return render(request, 'hiren.html', {'btn': login_btn, 'auth_button': nisha.authorized, 'id': nisha.id})


@login_required
def callback(request):
    """
    Handle github call back and then save the access token
    """
    if request.GET.get('code'):
        headers = {'Accept': 'application/json'}
        response = requests.post('https://github.com/login/oauth/access_token',
                                 {'client_id': settings.JSON_DATA['client_id'],
                                  'client_secret': settings.JSON_DATA['client_secret'],
                                  'code': request.GET.get('code'),
                                  'redirect_uri': settings.JSON_DATA['redirect_uri']}, headers=headers)
        api_res = response.json()
        obj = Hiren(access_token=api_res['access_token'], authorized=True)
        obj.save()
        return render(request, 'hiren.html', {'auth_button': True, 'id': obj.id})
    else:
        messages.error(request, "Ops ! Maybe a kitten died ! ")
        return render(request, 'hiren.html')


@login_required
def revoke(request, id):
    """
    Delete access token
    """
    obj = Hiren.objects.get(pk=id)
    obj.delete()
    return redirect('/hiren')
