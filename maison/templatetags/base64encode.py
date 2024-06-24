from django import template
import base64

register = template.Library()

@register.filter
def base64encode(value):
    return base64.b64encode(value).decode()