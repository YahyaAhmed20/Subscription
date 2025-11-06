from django.contrib import admin
from .models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_payment_date', 'is_paid')
    list_editable = ('is_paid',)
    search_fields = ('name',)
