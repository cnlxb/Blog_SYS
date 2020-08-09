from django import template
from ..models import *
register = template.Library()

@register.inclusion_tag('inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all()
    }