from django import forms
from django.views.generic import ListView
from crispy_forms.helper import FormHelper
from reference.models import Author, PublishingHous, Series_book, Genre_book


class AuthorListView(ListView):
    queryset = Author.objects.all()
    context_object_name = 'author'
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
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'


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
