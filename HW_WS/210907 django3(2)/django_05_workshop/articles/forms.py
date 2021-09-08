from articles.models import Article
from django import forms
   
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'maxlength': 10
            }
        )
    )
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'rows': 10,
                'cols': 50,
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'

