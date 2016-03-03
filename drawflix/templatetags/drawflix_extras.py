from django import template
from drawflix.models import Drawing

register = template.Library()

@register.inclusion_tag('drawflix/drawings.html')
def get_drawing_list():
    return {'drawings': Drawing.objects.all()}
