# forms.py
from django import forms
from .models import *
  
class PaintingsForm(forms.ModelForm):
  
    class Meta:
        model = Paintings
        fields = ['painting_Img']