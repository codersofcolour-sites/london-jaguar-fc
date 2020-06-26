from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from news.models import NewsIndexPage

class Galleries(Orderable):
    page = ParentalKey("gallery.GalleryPage", related_name="gallery_images")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image_caption = models.CharField(max_length=300, blank=True, null=True)
    
    panels = [
        ImageChooserPanel("image"),
        FieldPanel("image_caption"),
    ]
    

class GalleryPage(Page):
    intro = models.CharField(max_length=300, blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        MultiFieldPanel(
            [InlinePanel("gallery_images", label="Image"), ],
            heading="Gallery Images",
        )
    ]
