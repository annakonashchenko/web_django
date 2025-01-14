from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['full_name', 'email', 'comment_text']
        labels = {
            'full_name': 'Полное имя',
            'email': 'Электронная почта',
            'comment_text': 'Текст комментария',
        }
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Введите ваш комментарий...'
            }),
        }
