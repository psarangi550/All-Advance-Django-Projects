from django.contrib import admin

# Register your models here.
class BlogAdmin(admin.AdminSite):
    site_header="Pratik's Dashboard"
    index_header="Pratik's Dashboard"
    site_title="Dashboard"

blog_site=BlogAdmin(name="BlogAdminInterface")

