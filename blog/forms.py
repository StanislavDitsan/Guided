from .models import Comment, Post, Category, Contact
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


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class ImageUploadForm(forms.Form):
    image = forms.ImageField()