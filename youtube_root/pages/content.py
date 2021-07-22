from django import forms
from .models import Post

class ContentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','maintext', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Add your Title here"}),
            'maintext': forms.Textarea(attrs={'class': 'form-control' 'post-text', 'placeholder': "Add your content here"}),
        }