from django import forms
from django.forms import DateInput
from django.views.generic import ListView
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from reference.models import Author, PublishingHous, Series_book, Genre_book


class AuthorListView(ListView):
    queryset = Author.objects.all()
    context_object_name = 'author'
    list_filter = 'author'
    search_fields = ('name', 'surname')
    template_name = 'reference/author_list.html'


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'second_name',
            'surname',
            'date_birth',
            'date_death',
        ]

    def __init__(self, *args, **kwargs):
        super(AddAuthorForm, self).__init__(*args, **kwargs)
        self.fields['date_birth'].widget = DateInput(
            attrs={'type': 'date'})
        self.fields['date_death'].widget = DateInput(
            attrs={'type': 'date'})
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.add_input(
            Submit('submit', 'Add author', css_class='btn-primary'))


class PublhListView(ListView):
    queryset = PublishingHous.objects.all()
    context_object_name = 'publh'
    template_name = 'reference/publh_list.html'


class AddPublhForm(forms.ModelForm):
    class Meta:
        model = PublishingHous
        fields = [
            'name',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super(AddPublhForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.add_input(
            Submit('submit', 'Add publication hous', css_class='btn-primary'))


class SeriesListView(ListView):
    queryset = Series_book.objects.all()
    context_object_name = 'series'
    template_name = 'reference/series_list.html'


class AddSeriesForm(forms.ModelForm):
    class Meta:
        model = Series_book
        fields = [
            'name',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super(AddSeriesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.add_input(
            Submit('submit', 'Add Series', css_class='btn-primary'))


class GenreListView(ListView):
    queryset = Genre_book.objects.all()
    context_object_name = 'genre'
    template_name = 'reference/genre_list.html'


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre_book
        fields = [
            'name',
            'description',
        ]

    def __init__(self, *args, **kwargs):
        super(AddGenreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'POST'
        self.helper.add_input(
            Submit('submit', 'Add Genre', css_class='btn-primary'))
