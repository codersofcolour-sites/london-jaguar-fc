# Generated by Django 3.0.4 on 2020-06-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_auto_20200629_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialspage',
            name='intro',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
