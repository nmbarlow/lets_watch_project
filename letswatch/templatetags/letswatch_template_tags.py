from django import template
from letswatch.models import Genre

register = template.Library()

@register.inclusion_tag('letswatch/gens.html')
def get_genre_list():
    return {'gens':Genre.objects.all()}
