from django import forms
from .models import Action
from django.forms import ModelForm
 

class CustomDateForm(forms.Form):
    date=forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))


class ActionForm(ModelForm):
    class Meta:
        model=Action
        fields=('action','start_time','end_time','date','status')

        widgets={
            'start_time':forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'end_time':forms.TimeInput(attrs={'class':'form-control','type':'time'}),
            'date':forms.DateInput(attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            
        }
