from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.views.generic import TemplateView
from django.contrib.auth import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("django.contrib.auth.urls")),
    path('accounts/profile/',TemplateView.as_view(template_name="registration/profile.html"),name="profile"),
    url('', include('social_django.urls', namespace='social')),
]
