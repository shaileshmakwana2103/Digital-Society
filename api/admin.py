from django.contrib import admin
from .models import *
# Register your models here.
class AdminNotice(admin.ModelAdmin):
    list_display = ("id","title" , "description")
    search_fields = ('title',) 
    list_per_page = 5
    
    
    
    
admin.site.register(Notice,AdminNotice)

class AdminEvent(admin.ModelAdmin):
    list_display = ("id","title" , "description")
    search_fields = ('title',) 
    list_per_page = 5
admin.site.register(Event,AdminEvent)