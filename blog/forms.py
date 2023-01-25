from .models import Comment, Post, Category
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body', )


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'


class ImageUploadForm(forms.Form):
    image = forms.ImageField()