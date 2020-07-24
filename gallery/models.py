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
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    subpage_types = []
    max_count = 1 
    intro = models.CharField(max_length=300, blank=True, null=True)
    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        MultiFieldPanel(
            [InlinePanel("gallery_images", label="Image"), ],
            heading="Gallery Images",
        )
    ]
    
    def get_context(self, request, *args, **kwargs):
        context = super(GalleryPage, self).get_context(request, *args, **kwargs)
        live_newspages = self.gallery_images.all()
        all_pics = live_newspages
        paginator = Paginator(all_pics, 25)
        page = request.GET.get("page")
        
        try:
            pics = paginator.page(page)
        except PageNotAnInteger:
            pics = paginator.page(1)
        except EmptyPage:
            pics = paginator.page(paginator.num_pages)
        context["gallerypics"] = pics
        return context
