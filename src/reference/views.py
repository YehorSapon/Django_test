from django.views import generic
from . import forms
from reference import models
from django.urls import reverse_lazy
# from django.shortcuts import render
# from django.http import HttpResponseRedirect


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
# Author views


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
    template_name = "reference/author_del.html"
    model = models.Author
    success_url = "/reference/author/list/"


class AuthorAdd(generic.CreateView):
    template_name = "reference/author_add.html"
    model = models.Author
    form_class = forms.AddAuthorForm
    #success_url = "/reference/author-list/"

    def get_success_url(self):
        return reverse_lazy("reference:author", kwargs={'pk': self.object.pk})


"""
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
        return HttpResponseRedirect(request, 'reference/author/add/<int:pk>')
    elif request.method == 'GET':
        author = models.Author.objects.get(pk=pk)
        form = forms.AddAuthorForm(author)
        return render(request, 'item_add.html', context={'author': author, 'form': form})
"""

# Publising House


class PublhList(generic.ListView):
    template_name = "reference/publh_list.html"
    model = models.PublishingHous


class PublhView(generic.DetailView):
    template_name = "reference/publh.html"
    model = models.PublishingHous


class PublhEdit(generic.UpdateView):
    template_name = "reference/publh_add.html"
    model = models.PublishingHous
    form_class = forms.AddPublhForm
    success_url = "/reference/publh/list/"


class PublhDelete(generic.DeleteView):
    template_name = "reference/publh_del.html"
    model = models.PublishingHous
    success_url = "/reference/publh/list/"


class PublhAdd(generic.CreateView):
    template_name = "reference/publh_add.html"
    model = models.PublishingHous
    form_class = forms.AddPublhForm

    def get_success_url(self):
        return reverse_lazy("reference:publh", kwargs={'pk': self.object.pk})

# Series


class SeriesList(generic.ListView):
    template_name = "reference/series_list.html"
    model = models.Series_book


class SeriesView(generic.DetailView):
    template_name = "reference/series.html"
    model = models.Series_book


class SeriesEdit(generic.UpdateView):
    template_name = "reference/series_add.html"
    model = models.Series_book
    form_class = forms.AddSeriesForm
    success_url = "/reference/series/list/"


class SeriesDelete(generic.DeleteView):
    template_name = "reference/series_del.html"
    model = models.Series_book
    success_url = "/reference/series/list/"


class SeriesAdd(generic.CreateView):
    template_name = "reference/series_add.html"
    model = models.Series_book
    form_class = forms.AddSeriesForm

    def get_success_url(self):
        return reverse_lazy("reference:series", kwargs={'pk': self.object.pk})

# Genres


class GenreList(generic.ListView):
    template_name = "reference/genre_list.html"
    model = models.Genre_book


class GenreView(generic.DetailView):
    template_name = "reference/genre.html"
    model = models.Genre_book


class GenreEdit(generic.UpdateView):
    template_name = "reference/genre_add.html"
    model = models.Genre_book
    form_class = forms.AddGenreForm
    success_url = "/reference/genre/list/"


class GenreDelete(generic.DeleteView):
    template_name = "reference/genre_del.html"
    model = models.Genre_book
    success_url = "/reference/genre/list/"


class GenreAdd(generic.CreateView):
    template_name = "reference/genre_add.html"
    model = models.Genre_book
    form_class = forms.AddGenreForm

    def get_success_url(self):
        return reverse_lazy("reference:genre", kwargs={'pk': self.object.pk})
