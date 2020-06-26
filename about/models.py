from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
class AboutPage(Page):
    heading = models.CharField(blank=True, max_length=150)
    intro_text= models.CharField(blank=True, max_length=350)
    about_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL
    )    
    about_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic'])),
    ], null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('heading'),
                FieldPanel('intro_text')
            ], heading="Page Header"
        ),
        ImageChooserPanel('about_image'),
        StreamFieldPanel('about_content')            
    ]