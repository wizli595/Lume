
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write a comment...',
                'class': 'w-full p-3 rounded bg-black/20 text-white border border-purple-500'
            })
        }
