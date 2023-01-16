from django.contrib import admin
from .models import Orders

# Register your models here.
@admin.register(Orders)
class AdminJewelryType(admin.ModelAdmin):
    list_display = ['firstname','secondname','patronymic','address','type']
    list_display_links = list_display
    search_fields = list_display
