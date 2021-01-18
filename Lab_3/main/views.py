import os
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html', {'parameter': "test"})


def health(request):
    response = {
        'dateTime': datetime.now(),
        'serverUrl': request.build_absolute_uri(),
        'serverName': os.name, 
        'serverPid': os.getpid(),
        'clientAgent': request.META['HTTP_USER_AGENT'],
        'clientIp': request.META['REMOTE_ADDR'],
    }
    return JsonResponse(response)