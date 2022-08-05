from book.models import BookCard
from django import forms
from django.views.generic import ListView
from django.urls import reverse_lazy
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'book'
        self.helper.help_text_inline = True
        self.helper.add_input(Submit('submit', 'Submit'))
