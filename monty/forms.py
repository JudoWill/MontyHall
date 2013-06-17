__author__ = 'will'
from django import forms


class GuessForm(forms.Form):

    guess = forms.ChoiceField(choices=[(1, 1), (2, 2), (3, 3)],
                              widget=forms.RadioSelect)

