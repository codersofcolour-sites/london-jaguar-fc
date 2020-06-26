from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel

class ServicesPage(Page):
    heading = models.CharField(blank=True, max_length=150)
    intro_text= models.CharField(blank=True, max_length=350)

    content_panels = Page.content_panels + [
      FieldPanel('heading'),    
      FieldPanel('intro_text'),    
    ]