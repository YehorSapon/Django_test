from django import forms
from django.views.generic import ListView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from book.models import BookCard


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
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
