from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from book import models
from . import forms

# Create your views here.


class BookList(generic.ListView):
    template_name = "book/book_list.html"
    model = models.BookCard


class BookView(generic.DetailView):
    template_name = "book/book.html"
    model = models.BookCard


class BookEdit(LoginRequiredMixin, generic.UpdateView):
    template_name = "book/book_add.html"
    model = models.BookCard
    form_class = forms.AddBookForm
    success_url = "book/books/list/"


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
