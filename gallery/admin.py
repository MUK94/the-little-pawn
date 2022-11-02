from django.contrib import admin

from .models import GalleryColOne, GalleryColThree, GalleryColTwo


@admin.register(GalleryColOne)
class Gal1Admin(admin.ModelAdmin):
    list_display = ('caption', 'photo')

@admin.register(GalleryColTwo)
class Gal2Admin(admin.ModelAdmin):
    list_display = ('caption', 'photo')

@admin.register(GalleryColThree)
class Gal3Admin(admin.ModelAdmin):
    list_display = ('caption', 'photo')