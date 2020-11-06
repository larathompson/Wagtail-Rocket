from django.db import models

from wagtail.core.models import Page

from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
  # pass measn its not doing amnything
    # pass
  #  these are the names of the column
  #this is django as its coming from model.

  lead_text = models.CharField(
    # 150 chracter max
        max_length=140,
        # it ca n be blank
        blank=True,
        help_text='Subheading text under the banner title',
  )

  button = models.ForeignKey(
    # this adds a link to another wagtail page - this foreign key
        'wagtailcore.Page',
        # this is optional
        blank=True,
        # it can have nothing in database
        null=True,
        related_name='+',
        help_text='Select an optional page to link to',
        # what do we do when the page we are linking to is deleted - set null
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
