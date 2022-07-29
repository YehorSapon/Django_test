from django.utils.timezone import datetime
from django.shortcuts import render, redirect
from y_bookside.forms import LogMessageForm
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "y_bookside/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["date"] = datetime.now
        return context


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