# Generated by Django 3.0.4 on 2020-06-29 08:59

from django.db import migrations
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialspage',
            name='testimonials_video',
            field=wagtail.core.fields.StreamField([('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media'))], blank=True, null=True),
        ),
    ]