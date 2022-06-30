from .models import Books
from django import forms

class BookModelform(forms.ModelForm):
    class Meta:
        model=Books
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'picture':forms.FileInput(attrs={'class':'form-control'}),
            'auther':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),
        }
