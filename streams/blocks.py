from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock

class ParagraphBlock(blocks.StructBlock):
  paragraph = blocks.RichTextBlock(required=True, help_text='Add a paragraph')

  class Meta:
    template = 'streams/paragraph_block.html'
    icon= 'edit'
    label = "Add Paragraph"

class EmbedBlock(blocks.StructBlock):
  embed = EmbedBlock(required=True, help_text='Add media link')

  class Meta:
    template = 'streams/embed_block.html'
    icon= 'media'
    label = "Embed Media"

class QuoteBlock(blocks.StructBlock):
  quote = blocks.CharBlock(min_length=5, required=True, help_text='Add quote')

  class Meta:
    template = 'streams/quote_block.html'
    icon= 'openquote'
    label = "Add Quote"