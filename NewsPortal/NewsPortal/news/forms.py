from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class FormPost(forms.ModelForm):
    title = forms.CharField(min_length=20)

    class Meta:
       model = Post
       fields = ['title', 'author', 'postCategory', 'text']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        name = cleaned_data.get("text")

        if title == name:
            raise ValidationError(
                "Описание и текст не должны совпадать"
            )

        return cleaned_data
