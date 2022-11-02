from django.contrib import admin
from .models import Partners, Link

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo', 'url')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')