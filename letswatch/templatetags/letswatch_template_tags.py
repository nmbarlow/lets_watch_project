from django import template
from letswatch.models import Genre,Review

register = template.Library()

@register.inclusion_tag('letswatch/gens.html')
def get_genre_list():
    return {'gens':Genre.objects.all()}



def get_review_list():
    return {'reviews':Review.objects.all()}