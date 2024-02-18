from django.contrib import admin
from sousvk.models import svk

class sou(admin.ModelAdmin):
   list_display=('icon','title','description') 
   
   
admin.site.register(svk,sou)   

# Register your models here.
