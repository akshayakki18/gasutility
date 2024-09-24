from django.contrib import admin
from .models import servicelist, serviceform

class ServiceFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'service_request_type', 'submission_date', 'status')
    list_filter = ('service_request_type', 'status')
    search_fields = ('name', 'email', 'subject')

admin.site.register(servicelist)
admin.site.register(serviceform, ServiceFormAdmin)
