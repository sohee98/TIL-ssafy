from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the title',
            }
        )
    )
    overview = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the overview',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    poster_path = forms.CharField(
        max_length=500,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter the path',
            }
        )
    )
    class Meta:
        model = Movie
        fields = '__all__'