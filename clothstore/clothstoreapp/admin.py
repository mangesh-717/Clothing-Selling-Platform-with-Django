from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(Mensclothes)
admin.site.register(Ladiesclothes)



class CartEntriesAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_selected_products']

    def display_selected_products(self, obj):
        if obj.ladies_cloth_cart:
            return obj.ladies_cloth_cart.Ladies_cloth_name
        elif obj.men_cloth_cart:
            return obj.men_cloth_cart.mensclothes
        else:
            return "No product selected"

    display_selected_products.short_description = 'Selected Products'

admin.site.register(cartentrties, CartEntriesAdmin)

class OrderedEnteryAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_selected_products']

    def display_selected_products(self, obj):
        if obj.ladies_cloth_cart:
            return obj.ladies_cloth_cart.Ladies_cloth_name
        elif obj.men_cloth_cart:
            return obj.men_cloth_cart.mensclothes
        else:
            return "No product selected"

    display_selected_products.short_description = 'Selected Products'

admin.site.register(Orderedd, OrderedEnteryAdmin)

