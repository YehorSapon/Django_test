from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from book import models
from book import forms
from reference import models as m

# Create your views here.


class BookList(generic.ListView):
    template_name = "book/book_list.html"
    model = models.BookCard

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class BookView(generic.DetailView):
    template_name = "book/book.html"
    model = models.BookCard

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        authors = self.object.author.all()
        genres = self.object.genre
        publishings = self.object.publ_hous

        series = self.object.series
        print(series)
        if series:
            series_m = m.Series_book.objects.get(name=series)
            print(series_m)
        else:
            series_m = ""
        context['authors'] = authors
        context['genres'] = genres
        context['publishings'] = publishings
        context['series'] = series_m
        return context


class BookEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "book/book_edit.html"
    model = models.BookCard
    form_class = forms.AddBookForm
    success_url = "/book/books/list/"


class BookDelete(LoginRequiredMixin, generic.DeleteView):
    template_name = "book/book_del.html"
    model = models.BookCard
    success_url = "book/books/list/"


class BookAdd(LoginRequiredMixin, generic.CreateView):
    template_name = "book/book_add.html"
    model = models.BookCard
    form_class = forms.AddBookForm
    # success_url = "books/book-list/"

    def get_success_url(self):
        return reverse_lazy("book:book", kwargs={'pk': self.object.pk})
