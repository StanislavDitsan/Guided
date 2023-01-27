from .models import Comment, Post, Category
from django import forms
from django_summernote.fields import SummernoteTextFormField


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body', )


class PostForm(forms.ModelForm):
    content = SummernoteTextFormField()

    class Meta:
        model = Post
        fields = '__all__'


class ImageUploadForm(forms.Form):
    image = forms.ImageField()