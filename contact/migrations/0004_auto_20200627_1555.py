# Generated by Django 3.0.4 on 2020-06-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20200627_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactpage',
            name='address',
            field=models.CharField(blank=True, max_length=550),
        ),
    ]