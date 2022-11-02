from django.db import models

class GalleryColOne(models.Model):
    caption = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='gallery/img')

class GalleryColTwo(models.Model):
    caption = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='gallery/img')

class GalleryColThree(models.Model):
    caption = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='gallery/img')