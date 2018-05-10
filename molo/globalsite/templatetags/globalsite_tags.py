from django import template
from wagtail.wagtailcore.models import Site

register = template.Library()


@register.simple_tag(takes_context=True)
def current_country(context):
    request = context['request']
    current_site = Site.find_for_request(request)
    return current_site
