# Generated by Django 4.0.5 on 2022-10-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]