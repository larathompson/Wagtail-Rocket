from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
  # pass measn its not doing amnything
    # pass
  
    # lead_text = models.CharField (
    #   max_length=140, 
    #   blank=True, 
    #   help_text="Subheading text under banner title",
    # )

    # button = models.ForeignKey(
    #   # selecting wagtail key from the page core
    #   'wagtailcore.Page',
    #   blank=True,
    #   # can have nothing in databased
    #   null=True,
    #   related_name="+",
    #   help_text="Select an optional page to link to",
    #   # this tells django what to do when the link page has been deleted
    #   on_delete=models.SET_NULL,
    # )

    # button_text = models.CharField(
    #   max_length = 50,
    #   default ='Read More',
    #   # this alwasys has to be set even if button not sleected
    #   blank = False, 
    #   help_text = "Button text",

    # )

    # banner_background_image = models.ForeignKey(
    #   # this is linking it tot he default image
    #   'wagtailimages.Image',
    #   blank=False, 
    #   #  this means that this banner background image is allowed to be empty
    #   null=True,
    #   related_name="+",
    #   help_text = "The Banner Background Image",
    #   on_delete=models.SET_NULL,
    # )
  lead_text = models.CharField(
        max_length=140,
        blank=True,
        help_text='Subheading text under the banner title',
  )

  button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optional page to link to',
        on_delete=models.SET_NULL,
  )

  button_text = models.CharField(
        max_length=50,
        default='Read More',
        blank=False,
        help_text='Button text',
  )
  banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='The banner background image',
        on_delete=models.SET_NULL,
  )
  content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),

  ]
