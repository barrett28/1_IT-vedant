from django.contrib import admin
from .models import Recipe, Comment, Bookmark

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'ingredients']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'recipe', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text']

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'recipe', 'created_at']
    list_filter = ['created_at']