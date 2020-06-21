from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel 

@register_setting
class SiteSettings(BaseSetting):
  facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
  twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
  linkedin = models.URLField(blank=True, null=True, help_text="Linkedin URL")
  instagram = models.URLField(blank=True, null=True, help_text="Instagram URL")
  youtube = models.URLField(blank=True, null=True, help_text="Youtube channel URL")
  pinterest = models.URLField(blank=True, null=True, help_text="Pinterest URL")

  website_logo = models.ForeignKey(
    "wagtailimages.Image",
    null=True,
    blank=False,
    on_delete=models.SET_NULL,
    related_name="+",
  )
  
  panels = [
    MultiFieldPanel([
      FieldPanel('facebook'),
      FieldPanel('twitter'),
      FieldPanel('linkedin'),
      FieldPanel('instagram'),
      FieldPanel('youtube'),
      FieldPanel('pinterest'),
    ], heading="Social Media Settings"),
    ImageChooserPanel('website_logo')
  ]