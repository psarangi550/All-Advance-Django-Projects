from django.contrib import admin
from .models import AuthorModel
# Register your models here.
@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display=["id","author","name"]
