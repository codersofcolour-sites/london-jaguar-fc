from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel 

@register_setting(icon='site')
class SocialMediaSettings(BaseSetting):
  facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
  twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
  linkedin = models.URLField(blank=True, null=True, help_text="Linkedin URL")
  instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
  youtube = models.URLField(blank=True, null=True, help_text="Youtube channel URL")
  pinterest = models.URLField(blank=True, null=True, help_text="Pinterest URL")
  google = models.URLField(blank=True, null=True, help_text="Google acount URL")

  panels = [
    FieldPanel('facebook'),
    FieldPanel('twitter'),
    FieldPanel('linkedin'),
    FieldPanel('instagram'),
    FieldPanel('youtube'),
    FieldPanel('pinterest'),
    FieldPanel('google'),
  ]

  class Meta:
    verbose_name = 'social media accounts'

@register_setting(icon='image')
class WebsiteLogo(BaseSetting):
  website_logo = models.ForeignKey(
    "wagtailimages.Image",
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name="+",
  )

  panels = [
    ImageChooserPanel('website_logo'),
  ]

  class Meta:
    verbose_name = 'Website Logo'