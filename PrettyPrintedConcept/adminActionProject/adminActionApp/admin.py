from django.contrib import admin
from .models import Student
# Register your models here.

# @admin.action(description='Make is good Bad')




class  StudentAdmin(admin.ModelAdmin):
    list_display=["id","name","is_passed"]
    actions=["make_fail"]

    # @admin.action(description='Make it Bad')
    def make_fail(self,request,queryset):
         # return self.is_passed=False
         queryset.update(is_passed=False)
         # for instance in queryset:
         #    instance.is_passed=False
    make_fail.short_description="Make it False"

    # @admin.action()


admin.site.register(Student,StudentAdmin)
