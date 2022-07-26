from django.utils.timezone import datetime
from django.shortcuts import render, redirect


# Create your views here.

def home_page(request):
    context = {
            'date': datetime.now()
            }
    return render(request,
            'y_bookside/home.html',
            context)

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
        return render(request, "y_bookside/log_message.html", context)
