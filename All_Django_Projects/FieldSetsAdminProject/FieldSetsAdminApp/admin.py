from django.contrib import admin
from .models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=["id","title","desc"]
    fieldsets=(
            ("section1",
                {"fields":("title",),
                "description":"title of the field"}
                ),
            ("section2", {
                "fields":("desc",),
                "description":"description of the field"}
                )
            )

