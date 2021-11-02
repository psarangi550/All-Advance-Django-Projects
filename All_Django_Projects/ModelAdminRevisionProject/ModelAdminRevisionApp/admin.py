from django.contrib import admin
from .models import Blog
from django.contrib.admin import SimpleListFilter
# # Register your models here.

# class BlogAdmin(admin.AdminSite):
#     list_display=["user","title","description"]
#     search_fields=("title",'description')

class CustFilter(SimpleListFilter):
    title="Model Filter"
    parameter_name="title"
    def lookups(self,request,model_admin):
        return  [
           ("has_email","has_email"),
            ("no_email", "no_email"),
        ]
    def queryset(self,request,queryset):
        if self.value()=='':
            return queryset
        if self.value()=="has_email":
            return queryset.exclude(user__email="")
        if self.value()=="no_email":
            return queryset.filter(user__email="")



# @admin.register(Blog)
class MyBlogAdmin(admin.ModelAdmin):
    list_display=["user","title","description","email"]
    # search_fields=("title",'description',)
    list_filter=("id",CustFilter,)

admin.site.register(Blog,MyBlogAdmin)
