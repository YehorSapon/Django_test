from django import forms
from django.forms import DateInput
from django.views.generic import ListView
from book.models import BookCard
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
#from django.urls import reverse_lazy


class BookListView(ListView):
    queryset = BookCard.objects.all()
    context_object_name = 'book'
    template_name = 'book/book_list.html'


class AddBookForm(forms.ModelForm):
    class Meta:
        model = BookCard
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        self.fields['publ_year'].widget = forms.DateInput(
            attrs={'type': 'date'})
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.add_input(
            Submit('submit', 'Add Book', css_class='btn-primary'))

class EditBookForm(forms.ModelForm):
    class Meta:
        model = BookCard
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditBookForm, self).__init__(*args, **kwargs)
        self.fields['publ_year'].widget = forms.DateInput(
            attrs={'type': 'date'})
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.add_input(
            Submit('submit', 'Save the changes in book card', css_class='btn-primary'))
