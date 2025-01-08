from django.contrib import admin
from .models import LandOwner, LandRecord

@admin.register(LandOwner)
class LandOwnerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

@admin.register(LandRecord)
class LandRecordAdmin(admin.ModelAdmin):
    list_display = ('location', 'size_in_acres', 'purchase_date', 'owner') 
