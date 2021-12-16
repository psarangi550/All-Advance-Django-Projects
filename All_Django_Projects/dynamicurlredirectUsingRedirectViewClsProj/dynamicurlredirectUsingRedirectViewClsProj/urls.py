"""dynamicurlredirectUsingRedirectViewClsProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from django.views.generic.base import RedirectView,TemplateView
from dynamicurlredirectUsingRedirectViewClsApp.views import MyRedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:id>/<str:path>/',TemplateView.as_view(template_name="dynamicurlredirectUsingRedirectViewClsApp/home.html"),name='home'),
    # url('^index/(?P<id>\d*)/(?P<path>\w+)/$',MyRedirectView.as_view(),name='index')
# ]
]
