# Generated by Django 3.0.4 on 2020-06-29 09:19

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='news_content',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic', 'ol', 'ul'], icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('quote', wagtail.core.blocks.StructBlock([('source', wagtail.core.blocks.CharBlock(classname='full', help_text='The source of where that quote came from.')), ('quote_text', wagtail.core.blocks.CharBlock(classname='full', help_text='Add quote.'))], icon='openquote')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media'))], null=True),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='news_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
    ]
