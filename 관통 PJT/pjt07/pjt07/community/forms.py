from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'content', 'rank',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        min_length=2,
        max_length=200,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    class Meta:
        model = Comment
        fields = ('content', )