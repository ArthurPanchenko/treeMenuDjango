from django.contrib import admin
from .models import Category, Menu


admin.site.register(Menu)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'root')