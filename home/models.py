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
from blog.models import BlogIndexPage

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
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5,
                         min_num=1, label="Image"), ],
            heading="Carousel Images",
        )
    ]

    def get_carousel_images(self):
        carousel_lst = []
        for image in self.carousel_images.all():
            if image.carousel_image  != None:
                carousel_lst.append(image)
        return carousel_lst

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        try:
            recent_blogs = self.get_children().exact_type(BlogIndexPage).first().get_children().live().order_by('-first_published_at')
            context['recent_blogs'] = recent_blogs[:3]
            return context
        except:
            return context
