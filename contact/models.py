from django.db import models
from wagtail.wagtailadmin.utils import send_mail
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField
)

class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')

class ContactPage(AbstractEmailForm):
    # This is the default path.
    # If ignored, Wagtail adds _landing.html to your template name
    landing_page_template = "contact/contact_page_landing.html"

    intro = RichTextField(blank=True, features=['bold', 'italic'])
    thank_you_text = RichTextField(blank=True,features=['bold', 'italic', 'link'])

    address = models.CharField(max_length=550,blank=True)
    contact_number = models.CharField(max_length=90, blank=True)
    contact_email = models.CharField(max_length=150, blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            FieldPanel("address"),
            FieldPanel("contact_number"),
            FieldPanel("contact_email"),
        ], heading="Address Detail Settings"),        
        InlinePanel('form_fields', label='Form Fields'),
        FieldPanel('thank_you_text'),
        FieldPanel('intro'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Email Notification Settings"),
    ]

    def get_form_fields(self):
        return self.form_fields.all()   

