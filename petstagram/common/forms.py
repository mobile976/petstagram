from django import forms
from petstagram.common.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Add a comment...'}),
        }