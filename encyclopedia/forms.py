from django import forms

class NameForm(forms.Form):
    q = forms.CharField(max_length=100)
