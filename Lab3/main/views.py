from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import requests
import sys


def main(request):
    return render(request, 'main.html', {'parameter': "test"})

def get_current_time():
    url = 'http://date.jsontest.com/'
    try:
        r = requests.get(url=url)
    except requests.exceptions.RequestException as e:
        raise ConnectionError
    d = r.json()
    str_time = d['date']+' '+d['time']
    return str_time

def health(request):
    response = {'date': get_current_time(), 'current_page': request.build_absolute_uri(), 'server_info': request.META['SERVER_NAME'] + " " + sys.platform, 'client_info': request.META['HTTP_USER_AGENT'] + "    IP:" + request.META['REMOTE_ADDR']}
    return JsonResponse(response)
