"""
URL configuration for myfirstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from first_app import views
from users import views as userview
from users import router as user_api_router

api_url_patterns = [
    path(r'accounts/', include(user_api_router.router.urls))
]

urlpatterns = [
    path('api/', include(api_url_patterns)),
    path('', views.routeError),
    path('admin/', admin.site.urls),
    path('home/', views.index),
    path('users/', userview.users)
]

