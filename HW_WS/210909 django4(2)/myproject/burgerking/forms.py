from burgerking.models import Burgerking
from django import forms

class BurgerkingForm(forms.ModelForm):
    menu = forms.CharField(
        label='메뉴 이름',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Enter the menu',
                'maxlength': 10
            }
        )
    )
    
    C1 = 'burger'
    C2 = 'side'
    C3 = 'desert'
    category_choices = [(C1, '햄버거'), (C2,'사이드'), (C3,'음료&디저트')]
    category = forms.ChoiceField(choices=category_choices, widget=forms.Select())

    content = forms.CharField(
        label='정보',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Burgerking
        fields = '__all__'