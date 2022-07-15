
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world_view(request):
    return HttpResponse("<h1> Hello world! Current time </h1>")


def hello_there(request, name):
    return render(
        request,
        'hello_world/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
