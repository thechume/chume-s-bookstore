from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class Search(forms.Form):
    sterm = forms.DateField()

    def clean(self):
        data = self.cleaned_data['sterm']

        # Remember to always return the cleaned data.
        return data