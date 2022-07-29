#from django.views import generic
from django.http import HttpResponseRedirect
from django.views.generic import ListView
# from django.shortcuts import render, redirect
from . import forms
# from .models import Author
from . import models
# from . import forms
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

class AuthorList(ListView):
    template_name = "reference/all_item.html"
    model = models.Author

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs


    #def get_context_data(self, *args, **kwargs):
    #    context = super().get_context_data(*args, **kwargs)
    #    context["date"] = datetime.now
    #    return context


def add_author_view(request):
    if request.method == 'POST':
        form = forms.AddAuthorForm(request.POST)
        if form.is_valid():
           form.save()
    pass


def edit_author_view(request):
    if request.method == 'POST':
        form = forms.AddAuthorForm(request.POST)
        if form.is_valid():
           form.save()
        return HttpResponseRedirect(request, 'reference/author/{form.instance.pk}')
    elif request.method == 'GET':
        author = models.Author.objects.get(pk=pk)
        form = forms.AddAuthorForm(author)
        return render(request, 'item_add.html', context={'author': author, 'form': form})


'''
class AuthorDetail(generic.DetailView):
    template_name = 'reference/items_detal.html'
    model = models.Author
'''
