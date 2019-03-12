from django.shortcuts import render
from django.conf import settings


def index(request):
    context={
        'API_KEY':settings.MAPBOX_API,
    }
    return render(request,'front_end/index.html', context)

def additional(request):
    return render(request,'front_end/additional.html')