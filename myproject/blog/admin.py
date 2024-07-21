from django.contrib import admin

# Register your models here.

from .models import BlogPost , Category

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','updated_at']
    search_fields = ['title','description']
    list_filter = ['created_at','updated_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']