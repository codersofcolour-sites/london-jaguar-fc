# Generated by Django 3.0.4 on 2020-06-26 11:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields
import wagtail.embeds.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', models.CharField(max_length=150)),
                ('testimonials_video', wagtail.core.fields.StreamField([('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media'))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
