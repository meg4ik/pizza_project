from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

from pizza_app.models import PizzaOrder, PizzaSize

# Create your views here.

def index(request):
    if request.method == 'GET':
        pizzas = PizzaOrder.objects.all()
        return render(request, 'pizza_app/index.html', {'pizzas': pizzas})
    return HttpResponse(status=405)
def create():
    pass
def view():
    pass
def close():
    pass
def stats():
    pass