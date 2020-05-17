from django.contrib import admin

# Register your models here.
from .models import Store

class StoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

admin.site.register(Store,StoreAdmin)