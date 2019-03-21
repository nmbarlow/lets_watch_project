from django import template
from django.template import Template, Context
from letswatch.models import Genre,Review
from django.utils.safestring import mark_safe

register = template.Library()

@register.inclusion_tag('letswatch/gens.html')
def get_genre_list():
    return {'gens':Genre.objects.all()}


@register.inclusion_tag('letswatch/show_genresss.html')
def genre_template():
	return {'gens':Genre.objects.all()}


def get_review_list():
    return {'reviews':Review.objects.all()}