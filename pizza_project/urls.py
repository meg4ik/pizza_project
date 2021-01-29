"""pizza_project URL Configuration

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

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from pizza_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('pizza_auth_app.urls', namespace='pizza_auth')),
    path('pizza/', include('pizza_app.urls', namespace='pizza')),
    path('', index, name = 'index'),
    path('api/', include('rest_api_app.urls', namespace='rest_api_app')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
