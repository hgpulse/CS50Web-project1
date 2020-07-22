from django import forms
from django.utils.datastructures import MultiValueDict

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import entries

class EditForm(forms.Form):
    
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = entries 
  
        # specify fields to be used 
        fields = [ 
            "title", 
            "entry", 
        ] 

class NewForm(forms.Form):
    title = forms.CharField(label="Title", initial="Enter Title Here")
    entry = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":5, "cols":20}),initial="Enter Markdown Here")
    