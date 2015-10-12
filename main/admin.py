from django.contrib import admin
from main.models import Cereal, Manufacturer

#Register your models here.

class CerealAdmin(admin.ModelAdmin):
    search_fields = ['name', 'manufacturer']

class ManAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Cereal, CerealAdmin)
admin.site.register(Manufacturer, ManAdmin)