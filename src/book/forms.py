from book.models import BookCard
from django import forms
from django.views.generic import ListView
#from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class BookListView(ListView):
    queryset = BookCard.objects.all()
    context_object_name = 'book'
    template_name = 'book/book_list.html'


class AddBookForm(forms.ModelForm):
    class Meta:
        model = BookCard
        fields = '__all__'

    @property
    def helper(self):
        helper = FormHelper()
        helper.method = 'POST'
        helper.add_input(Submit('save', 'save'))
        return helper
