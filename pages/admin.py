from django.contrib.admin import register, ModelAdmin #register es un decorador, una funcion que modifica otra funcion
from .models import Page 

@register(Page)
class PageAdmin(ModelAdmin):   
    readonly_fields =('created','updated')
    list_display = ('title','ordering')

    

    