from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig
from .admin import BlogAdmin
from django.contrib import admin

class BlogAdminConfig(AdminConfig):
    default_site="AdminReplacementApp.admin.BlogAdmin"

class AdminreplacementappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AdminReplacementApp'
