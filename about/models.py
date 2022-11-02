from tokenize import blank_re
from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    heading = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='about/images/')

class Achievement(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)