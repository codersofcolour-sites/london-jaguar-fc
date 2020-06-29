from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

class TestimonialsPage(Page):
    subpage_types = []
    max_count = 1 
    intro = models.CharField(max_length=150, blank=True)
    testimonials_video = StreamField([
        ('embedded_video', EmbedBlock(icon="media")),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        StreamFieldPanel('testimonials_video'),
    ]
