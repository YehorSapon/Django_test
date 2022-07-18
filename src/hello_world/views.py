
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello_world.forms import LogMessageForm
from hello_world.models import LogMessage


# Create your views here.

def hello_world_view(request):
    return render(
        request,
        'hello_world/hello.html',
        {
            'date': datetime.now()
        }
    )


def hello_there(request, name):
    return render(
        request,
        'hello_world/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
