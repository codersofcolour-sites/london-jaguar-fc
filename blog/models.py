from django.db import models
from django.utils import timezone

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from wagtail.core.rich_text import expand_db_html, RichText


class BlogIndexPage(Page):
    subpage_types = ['BlogPage']
    intro = models.CharField(blank=True, max_length=150)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        live_blogpages = self.get_children().live()
        context['blogpages'] = live_blogpages.live().order_by('-first_published_at')
        return context


class BlogPage(Page):
    date = models.DateField("Post date")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    blog_content = StreamField([
        ('paragraph', blocks.RichTextBlock(icon="pilcrow")),
        ('image', ImageChooserBlock(icon="image")),
        ('quote', blocks.StructBlock([
            ('source', blocks.CharBlock(classname="full",
                                        help_text='The source of where that quote came from.')),
            ('quote_text', blocks.CharBlock(
                classname="full", help_text='Add quote.')),
        ], icon='openquote'), ),
        ('embedded_video', EmbedBlock(icon="media")),
    ], null=True)

    intro = models.CharField(max_length=250)
    
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('image'),
        FieldPanel('intro'),
        StreamFieldPanel('blog_content'),
    ]

BlogPage._meta.get_field("date").default = timezone.now