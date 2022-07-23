from django.utils.timezone import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from hello_world.forms import LogMessageForm



# Create your views here.

def hello_world_view(request):
    context = {
            'date': datetime.now()
            }
    return render(
        request,
        'hello_world/hello.html',
         context
    )


def hello_there(request, name):

    context = {
            'name': name,
            'date': datetime.now()
        }
    return render(
        request,
        'hello_world/hello_there.html',
        context
        )


def log_message(request):
    form = LogMessageForm(request.POST or None)
    context = {"form": form}
    if request.method == "POST":

        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello_world/log_message.html", context)
