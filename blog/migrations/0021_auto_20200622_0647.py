# Generated by Django 3.0.4 on 2020-06-22 05:47

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200621_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.core.blocks.RichTextBlock(icon='pilcrow')), ('quote', wagtail.core.blocks.StructBlock([('source', wagtail.core.blocks.CharBlock(classname='full', help_text='The source of where that quote came from.')), ('quote_text', wagtail.core.blocks.CharBlock(classname='full', help_text='Add quote.'))], icon='openquote')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media'))], null=True),
        ),
    ]
