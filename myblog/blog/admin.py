# blog/admin.py
from django.contrib import admin
from .models import Post, Comment

# Unregister the Post model if it has been registered elsewhere
try:
    admin.site.unregister(Post)
except admin.sites.NotRegistered:
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
