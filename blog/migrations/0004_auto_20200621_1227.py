# Generated by Django 3.0.4 on 2020-06-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
