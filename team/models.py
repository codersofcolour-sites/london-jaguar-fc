from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class TeamPage(Page):
    intro = models.CharField(blank=True, max_length=150)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
