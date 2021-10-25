from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        # 사용자에게 보여줄 & is_valid() 에서 검증할 필드들
        fields = ('title', 'content', 'rank',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        min_length=2,
        max_length=200,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    class Meta:
        model = Comment
        # 사용자에게 보여줄 & is_valid() 에서 검증할 필드들
        fields = ('content', )