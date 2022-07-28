from django.utils.timezone import datetime
from django.shortcuts import render, redirect
from y_bookside.forms import LogMessageForm


def home_page(request):
    context = {
            'date': datetime.now()
            }
    return render(request,
                  'y_bookside/home.html',
                  context=context)


def page_about(request):
    context = {
            'date': datetime.now(),
            'title': 'About',
            }
    return render(request,
                  'y_bookside/about.html',
                  context=context)


def page_contacts(request):
    context = {
            'date': datetime.now(),
            'title': 'Contacts',
            }
    return render(request,
                  'y_bookside/contacts.html',
                  context=context)


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
        return render(request, "y_bookside/log_message.html", context=context)
