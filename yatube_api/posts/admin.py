from django.contrib import admin

from .constants import MAX_STR_REPRESENTATION_LENGTH
from .models import Comment, Follow, Group, Post

admin.site.empty_value_display = 'Не задано'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('group',)
    list_per_page = MAX_STR_REPRESENTATION_LENGTH


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created')
    search_fields = ('text',)
    list_filter = ('created', 'author',)
    list_per_page = MAX_STR_REPRESENTATION_LENGTH


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    search_fields = ('title',)
    list_editable = ('slug',)
    list_per_page = MAX_STR_REPRESENTATION_LENGTH


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    search_fields = ('user',)
    list_per_page = MAX_STR_REPRESENTATION_LENGTH
