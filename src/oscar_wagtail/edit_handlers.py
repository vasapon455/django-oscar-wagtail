from django.utils.html import escape
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.rich_text.pages import PageLinkHandler as _PageLinkHandler

from oscar_wagtail import widgets


class ProductChooserPanel(FieldPanel):
    """Custom panel that renders the product chooser widget."""

    def __init__(self, field_name, product_type=None, **kwargs):
        super().__init__(field_name, **kwargs)
        self.product_type = product_type

    def clone(self):
        return self.__class__(
            field_name=self.field_name,
            product_type=self.product_type,
        )

    def widget_overrides(self):
        return {
            self.field_name: widgets.AdminProductChooser()
        }


class PageLinkHandler(_PageLinkHandler):
    """Override the default PageLinkHandler to make sure we use the url
    property of the `Category` classes.
    """

    @classmethod
    def expand_db_attributes(cls, attrs):
        try:
            page = Page.objects.get(id=attrs['id']).specific
            return '<a href="%s">' % escape(page.url)
        except Page.DoesNotExist:
            return "<a>"
