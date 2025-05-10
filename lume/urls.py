"""
URL configuration for lume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('', include('persona.urls')),
    path('article/', include('inkwell.urls')),
    path('feed/', include('pulse.urls')),
    path('echoes/', include('echoes.urls')),
    path('ai/', include('InkFuse.urls')),

path("__debug__/", include(debug_toolbar.urls)),
    path('__reload__/', include('django_browser_reload.urls')),
]
