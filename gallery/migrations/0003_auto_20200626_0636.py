# Generated by Django 3.0.4 on 2020-06-26 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20200626_0635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Galleries'},
        ),
    ]
