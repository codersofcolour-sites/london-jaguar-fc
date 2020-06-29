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

class HomePageCarousel(Orderable):
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    carousel_header = models.CharField(max_length=150, blank=True, null=True)
    carousel_text = models.CharField(max_length=300, blank=True, null=True)
    
    panels = [
        MultiFieldPanel([
            ImageChooserPanel("carousel_image"),
            FieldPanel("carousel_header"),
            FieldPanel("carousel_text"),   
        ], heading='Carousel')
]
    

class HomePage(Page):
    video_url = models.URLField(blank=False, null=True)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    header = models.CharField(max_length=150, blank=True, null=True)
    subheader = models.CharField(max_length=150, blank=True, null=True)
    content = models.CharField(max_length=550, blank=True, null=True)
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5,
                         min_num=1, label="Image"), ],
            heading="Carousel Images",
        ),
        MultiFieldPanel([
            FieldPanel("header"),
            FieldPanel("subheader"),   
            ImageChooserPanel("logo"),
            FieldPanel("content"),
            FieldPanel("video_url"),   
        ], heading='Hero Config')        
    ]

    def get_carousel_images(self):
        carousel_list = []
        for image in self.carousel_images.all():
            if image.carousel_image  != None:
                carousel_list.append(image)
        return carousel_list

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        try:
            recent_news = self.get_children().exact_type(NewsIndexPage).first().get_children().live().order_by('-first_published_at')
            context['recent_news'] = recent_news[:3]
            return context
        except:
            return context
