from django.contrib import admin
from .models import About, Achievement

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description', 'image')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    list_filter = ('title', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


