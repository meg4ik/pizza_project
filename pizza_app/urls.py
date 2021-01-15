from django.urls import path

from pizza_app.views import create, view, close, stats

app_name = 'pizza'
urlpatterns = [
    path('create/', create, name = 'create'),
    path(r'^view/(?P<pizza_order_id>[0-9]+)/', view, name = 'view'), 
    path(r'^close/(?P<pizza_order_id>[0-9]+)/', close, name = 'close'),
    path('stats/', stats, name = 'stats'),
]