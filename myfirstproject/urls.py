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
from django.conf.urls.static import static

from first_app import views
from users import views as userview
from users import router as user_api_router
from django.conf import settings
from house import router as house_api_router
from tasks import router as task_api_router

auth_api_urls = [
    path(r'', include('rest_framework_social_oauth2.urls')),
]

if settings.DEBUG:
    auth_api_urls.append(path(r'verify/', include('rest_framework.urls')))
api_url_patterns = [
    path(r'auth/', include(auth_api_urls)),
    path(r'accounts/', include(user_api_router.router.urls)),
    path(r'houses/', include(house_api_router.router.urls)), 
    path(r'tasks/', include(task_api_router.router.urls))
]

urlpatterns = [
    path('api/', include(api_url_patterns)),
    path('', views.routeError),
    path('admin/', admin.site.urls),
    path('home/', views.index),
    path('users/', userview.users),
    path('apis/', views.apis),
]

#For File Handling
urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

