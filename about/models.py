from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.rich_text import expand_db_html, RichText

class AboutPage(Page):   
    about_content = StreamField([
        ('subheading', blocks.RichTextBlock(icon="title", features=['h2'])),
        ('paragraph', blocks.RichTextBlock(icon="pilcrow", features=['p','link', 'bold', 'italic'])),
    ], null=True)

    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)

    content_panels = Page.content_panels + [
        StreamFieldPanel('about_content')            
    ]