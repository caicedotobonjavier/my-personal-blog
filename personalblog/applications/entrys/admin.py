from django.contrib import admin
#
from .models import Category, Entry
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display =(
        'name',
        'short_name',
    )


admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display =(
        'title',
        'resumen',
        'created',
        'active',
        'in_home',
        'user',
    )
    search_fields = (
        'title',
    )
    
    list_filter = (
        'active', 
        'in_home',
        'user',
    )


admin.site.register(Entry, EntryAdmin)