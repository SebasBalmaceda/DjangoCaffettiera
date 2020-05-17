from django import template
from pages.models import Page

register = template.Library()
    
@register.simple_tag  #una funcion decoradora recibe una funcion como parametro y devuelve otra
def get_page_list():
    pages = Page.objects.all()              
    return pages