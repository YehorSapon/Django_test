from django import forms
from reference.models import Author, PublishingHous, Series_book, Genre_book
from django.views.generic import ListView


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
