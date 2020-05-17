from .models import Link

def contexto_propio(request):
    context = {}                 #diccionario vacio
    for link in Link.objects.all():
        context[link.key] = link.url
    return context
    
#pasamos un diccionario al contexto global
