# Generated by Django 3.0.4 on 2020-06-25 20:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailimages', '0022_uploadedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.CharField(blank=True, max_length=150)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='NewsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Post date')),
                ('news_content', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['p', 'link', 'bold', 'italic'], icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('quote', wagtail.core.blocks.StructBlock([('source', wagtail.core.blocks.CharBlock(classname='full', help_text='The source of where that quote came from.')), ('quote_text', wagtail.core.blocks.CharBlock(classname='full', help_text='Add quote.'))], icon='openquote')), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media'))], null=True)),
                ('news_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]