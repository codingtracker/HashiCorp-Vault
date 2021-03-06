"""ACG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from ACG_Login.views import acg_login_view, acg_login_view, home, api_auth_test

urlpatterns = [
    path('', home, name='home'),
    path('api_auth_test', api_auth_test, name='api_auth_test'),
    path('login', acg_login_view, name='acg_login'),
    path('admin/', admin.site.urls),
]
