from django.contrib import admin
from .models import Post, Comment, Category, Contact
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('content')
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on', 'author',
                    'updated_on')
    search_fields = [
        'title',
        'content',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approved_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)