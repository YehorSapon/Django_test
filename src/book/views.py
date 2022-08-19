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
        genres = self.object.genre.all()
        publh = self.object.publ_hous
        series = self.object.series.all()
        context['authors'] = authors
        context['genres'] = genres
        context['publh'] = publh
        context['series'] = series
        return context


class BookEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "book/book_edit.html"
    model = models.BookCard
    form_class = forms.EditBookForm
    login_url = reverse_lazy("user_app:login")
    success_url = "/book/books/list/"


class BookDelete(LoginRequiredMixin, generic.DeleteView):
    template_name = "book/book_del.html"
    model = models.BookCard
    success_url = "/book/books/list/"
    login_url = reverse_lazy("user_app:login")


class BookAdd(LoginRequiredMixin, generic.CreateView):
    template_name = "book/book_add.html"
    model = models.BookCard
    form_class = forms.AddBookForm
    login_url = reverse_lazy("user_app:login")
    success_url = "books/book-list/"

    def get_success_url(self):
        return reverse_lazy("book:book", kwargs={'pk': self.object.pk})
