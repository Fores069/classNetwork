from django import template
from main.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('main/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats':cats, 'cat_selected':cat_selected}

@register.simple_tag()
def get_posts():
    return Posts.objects.all()

