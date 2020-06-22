# Generated by Django 3.0.4 on 2020-06-22 21:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200622_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('quote', wagtail.core.blocks.StructBlock([('source', wagtail.core.blocks.CharBlock(classname='full', help_text='The source of where that quote came from.')), ('quote_text', wagtail.core.blocks.CharBlock(classname='full', help_text='Add quote.'))], icon='openquote')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media'))], null=True),
        ),
    ]