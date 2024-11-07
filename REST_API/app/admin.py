from django.contrib import admin
from .models import ModelDataTables 
# Register your models here.



class modeldatatable(admin.ModelAdmin):

    list_display  = ['user' , 'item_name']

admin.site.register(ModelDataTables , modeldatatable)
