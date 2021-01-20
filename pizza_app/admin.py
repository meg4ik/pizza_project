from django.contrib import admin

# Register your models here.

from pizza_app.models import Address

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'full', )


# PizzaIngredient
# PizzaMenuItem
# PizzaSize
# PizzaOrder

# list_display
# search
#

admin.site.register(Address, AddressAdmin)