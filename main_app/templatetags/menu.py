from django import template
from main_app.models import Category, Menu

register = template.Library()


@register.inclusion_tag('main_app/tags/nav.html')
def draw(title):
    root_categories = Category.objects.filter(menu__title=title, root=None)
    return {'categories': root_categories}