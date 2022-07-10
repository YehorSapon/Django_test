from time import strftime
import datetime
from django.shortcuts import render, HttpResponse

# Create your views here.


now = datetime.datetime.now()
time_string = strftime("%H:%M:%S")


def hello_world_view(request):
    return HttpResponse(f"<h1> Hello world! Current time {time_string}</h1>")
