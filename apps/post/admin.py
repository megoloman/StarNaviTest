from django.contrib import admin

from apps.post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'likes', 'dislikes', 'created_at', 'updated_at')
