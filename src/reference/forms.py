from django import forms
from reference import models
from reference.models import Author
from django.views.generic import ListView


class AuthorListView(ListView):
    queryset = Author.objects.all()
    context_object_name = 'author'
    template_name = 'reference/list_author.html'


class AddAuthorForm(forms.ModelForm):

    class Meta:
        model = models.Author
        fields = [
            'name',
            'second_name',
            'surname',
            'date_birth',
            'date_death',
            ]




'''  name = forms.CharField(
        max_length=25,
        help_text="Enter author name",
        )
    second_name = forms.CharField(
        max_length=25,
        help_text="Enter author name",
        required=False,
       )
    surname = forms.CharField(
        max_length=25,
        help_text="Enter author surname",
        )
    date_birth = forms.DateField(
        help_text="Enter author's birth year",
        required=False,
        )
    date_death = forms.DateField(
        help_text="Enter author's year of death",
        required=False,
        )
'''
