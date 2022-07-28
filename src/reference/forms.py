from django import forms


class AddAuthorForm(forms.Form):
    name = forms.CharField(
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
