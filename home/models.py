from django.db import models


class Partners(models.Model):
    name = models.CharField(max_length=40)
    logo = models.ImageField(upload_to='partners/img')
    url = models.URLField(blank=True)

class Link(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField(blank=False)
