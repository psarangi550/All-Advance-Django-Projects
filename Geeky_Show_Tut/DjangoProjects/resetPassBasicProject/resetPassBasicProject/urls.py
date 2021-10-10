"""resetPassBasicProject URL Configuration

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
from django.urls import path
from resetPassBasicApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view ,name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('setpass/', views.set_password_view, name="setpass"),
    path('passchange/',views.password_change_view, name="passchange"),
    path('userchange/',views.user_change_view, name="userchange"),
    path('password/',views.password_change_view, name="password"),
]
