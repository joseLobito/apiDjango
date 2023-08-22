from django.contrib import admin
from categories.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','published']