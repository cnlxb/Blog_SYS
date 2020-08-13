from django import template
from django.db.models.aggregates import Count
from ..models import *
register = template.Library()

@register.inclusion_tag('inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return {
        'category_list': category_list,
    }