from django.contrib import admin
from troncal.models import Foodf, Focable,Fodio

# Register your models here.

class FoodfAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'geometria')

admin.site.register(Foodf,FoodfAdmin)
admin.site.register(Focable)
admin.site.register(Fodio)
