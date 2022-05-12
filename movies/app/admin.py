from django.contrib import admin

from .models import Comment, Movie

# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "Title")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
