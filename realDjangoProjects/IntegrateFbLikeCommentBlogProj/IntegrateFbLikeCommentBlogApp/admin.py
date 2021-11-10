from django.contrib import admin
from .models import User,Blog
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=["id","author","published_date","blog_img","title","desc"]
