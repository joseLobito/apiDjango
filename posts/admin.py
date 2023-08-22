from django.contrib import admin
from posts.models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','user','created_at', 'published']
