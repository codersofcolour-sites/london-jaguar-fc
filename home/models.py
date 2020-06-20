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
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel    


class HomePageCarousel(Orderable):
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    carousel_header = models.CharField(max_length=50, blank=True, null=True)
    carousel_text = models.CharField(max_length=300, blank=True, null=True)
    panels = [
        ImageChooserPanel("carousel_image"),
        FieldPanel("carousel_header"),
        FieldPanel("carousel_text"),
    ]

class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Image"),],
            heading="Carousel Images",
        ),
        FieldPanel('body', classname="full"),
    ]
