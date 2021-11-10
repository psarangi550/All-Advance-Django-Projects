from django.contrib import admin
from .models import Video
from embed_video.admin import AdminVideoMixin
# Register your models here.

class VideoAdmin(AdminVideoMixin,admin.ModelAdmin):
    list_display=["name","date_added","url"]


admin.site.register(Video,VideoAdmin)
