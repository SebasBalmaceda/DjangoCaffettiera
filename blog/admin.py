from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display= ('title', 'author', 'published')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')#tabla__campo siempre dos guiones bajos
    list_filter = ('author__username', 'categories__name') #relacion muchos a muchos

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)