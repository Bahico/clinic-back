from django.contrib import admin

from partner.models import PartnerModel


# Register your models here.

@admin.register(PartnerModel)
class PartnerModelAdmin(admin.ModelAdmin):
    list_display = ('id','image','pdf')

