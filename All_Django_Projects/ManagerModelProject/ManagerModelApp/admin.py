from django.contrib import admin
from .models import Post,PostProxy
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=["id","created","updated"]

@admin.register(PostProxy)
class PostProxyAdmin(admin.ModelAdmin):
    list_display=["id","created","updated"]
