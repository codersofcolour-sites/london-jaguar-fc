# Generated by Django 3.0.4 on 2020-06-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0003_socialmediasettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='google',
            field=models.URLField(blank=True, help_text='Google acount URL', null=True),
        ),
    ]
