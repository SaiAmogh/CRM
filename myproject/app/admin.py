from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=['category']


admin.site.register(Product,ProductAdmin)
admin.site.site_header='Amogh Dashboard'
admin.site.register(Order)
