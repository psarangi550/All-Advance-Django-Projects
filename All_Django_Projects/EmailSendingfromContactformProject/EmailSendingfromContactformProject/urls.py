"""EmailSendingfromContactformProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    2. Add an import:  from my_app import views
    3. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    2. Add an import:  from other_app.views import Home
    3. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    2. Import the include() function: from django.urls import include, path
    3. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EmailSendingfromContactformApp import views
urlpatterns = [
path('admin/', admin.site.urls),
path('', views.index_view,name="home"),
]
