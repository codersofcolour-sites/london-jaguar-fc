# Generated by Django 3.0.4 on 2020-06-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_aboutpage_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='heading',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='aboutpage',
            name='intro_text',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
