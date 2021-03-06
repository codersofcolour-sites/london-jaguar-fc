# Generated by Django 3.0.4 on 2020-06-25 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('site_settings', '0002_sitesettings_pinterest'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Facebook URL', null=True)),
                ('twitter', models.URLField(blank=True, help_text='Twitter URL', null=True)),
                ('linkedin', models.URLField(blank=True, help_text='Linkedin URL', null=True)),
                ('instagram', models.URLField(blank=True, help_text='Instagram URL', null=True)),
                ('youtube', models.URLField(blank=True, help_text='Youtube channel URL', null=True)),
                ('pinterest', models.URLField(blank=True, help_text='Pinterest URL', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'social media accounts',
            },
        ),
    ]
