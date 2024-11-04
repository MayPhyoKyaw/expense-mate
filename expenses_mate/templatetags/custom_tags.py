# expenses_mate/templatetags/custom_tags.py
from django import template # type: ignore

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    try:
        return field.as_widget(attrs={'class': css_class})
    except AttributeError:
        return field