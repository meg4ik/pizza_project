from django.urls import path

from pizza_app.views import create, view, close, stats

app_name = 'pizza'
urlpatterns = [
    path('create/', create, name = 'create'),
    path(r'view/<pizza_order_id>/', view, name = 'view'), 
    path(r'close/<pizza_order_id>/', close, name = 'close'),
    path('stats/', stats, name = 'stats'),
]