from django.contrib import admin
from .models import Actor, Movie, Comment


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthdate', 'gender',)
    list_filter = ('gender',)


@admin.register(Movie)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'genre',)
    list_filter = ('genre',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'text', 'created_date')