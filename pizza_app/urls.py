from django.urls import path

from pizza_app.views import create, view, close, stats

urlpatterns = [
    path('create/', create, name = 'create'),
    path('view/', view, name = 'view'),
    path('close/', close, name = 'close'),
    path('stats/', stats, name = 'stats'),
]