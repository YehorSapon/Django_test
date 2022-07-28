from django.views import generic
# from django.shortcuts import render, redirect
# from .forms import AddAuthorForm
# from .models import Author
from . import models
 from . import forms
# Create your views here.

'''
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            # print(form.changed_data)
            try:
                Author.objects.create(**form.changed_data)
                return redirect('home')
            finally:
                form.add_error(None, 'error of add author')
    else:
        form = AddAuthorForm()

    context = {
        'title': 'Add Author',
        'form': form,
    }
    return render(request,
                  'reference/add_author.html', context=context)
'''

def add_author(request):
    pass

class AuthorDetail(generic.DetailView):
    template_name='reference/items_detal.html'
    model = models.Author

class AuthorAdd(generic.CreateView):
    template_name = 'reference/items_edit.html'
    form_class =
    form.AddAuthorForm
    model = models.Author
