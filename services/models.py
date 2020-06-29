from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import StreamFieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.rich_text import expand_db_html, RichText

class Services(Orderable):
    page = ParentalKey("services.ServicesPage", related_name="services_list")
    subheading = models.CharField(max_length=150)
    paragraph = RichTextField(blank=False, features=['p'])
    
    panels = [
        FieldPanel('subheading'),
        FieldPanel('paragraph')
    ]
    

class ServicesPage(Page):
    subpage_types = []   
    max_count = 1 
    # Replace wrapped rich-text div
    RichText.__html__ = lambda self: expand_db_html(self.source)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("services_list", label="Service"), ],
            heading="Services",
        )
    ]