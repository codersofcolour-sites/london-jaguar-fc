# Generated by Django 3.0.4 on 2020-06-21 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200621_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 21, 13, 41, 17, 389252), verbose_name='Post date'),
        ),
    ]