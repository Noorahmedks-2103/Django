from django.contrib import admin
from .models import Product

class ProjectAdmin(admin.ModelAdmin):
    list_display=['name','price','quantity','brand']
    ordering=['id']
    search_fields=['name']

admin.site.register(Product,ProjectAdmin)
