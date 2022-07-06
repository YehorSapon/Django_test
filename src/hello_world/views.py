from django.shortcuts import render, HTTPResponse

# Create your views here.


def hello_world_view(request):
    return HTTPResponse('< h1 > Hello world < /h1 >')
