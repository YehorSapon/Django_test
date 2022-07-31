from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from . import forms
from reference import models
from django.urls import reverse_lazy


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


class AuthorList(generic.ListView):
    template_name = "reference/author_list.html"
    model = models.Author


class AuthorView(generic.DetailView):
    template_name = "reference/author.html"
    model = models.Author


class AuthorEdit(generic.UpdateView):
    template_name = "reference/author_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    success_url = "/reference/author/list/"


class AuthorDelete(generic.DeleteView):
    template_name = "reference/author-del.html"
    model = models.Author
    success_url = "/reference/author/list/"


class AuthorAdd(generic.CreateView):
    template_name = "reference/author_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    #success_url = "/reference/author-list/"

    def get_success_url(self):
        return reverse_lazy("reference:author", kwargs={'pk': self.object.pk})


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
