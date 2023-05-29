from django.contrib import admin

from bboard import models


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'service_type', 'cost')
    list_display_links = ('purchase_date', 'service_type')
    search_fields = ('purchase_date', 'service_type')


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'device_type', 'cost')
    list_display_links = ('purchase_date', 'device_type')
    search_fields = ('purchase_date', 'device_type')


admin.site.register(models.Bb, BbAdmin)
admin.site.register(models.Rubric)
admin.site.register(models.DeviceCost, DeviceAdmin)
admin.site.register(models.ServiceCost, ServiceAdmin)
admin.site.register(models.DeviceType)
admin.site.register(models.DeviceRoom)
admin.site.register(models.DeviceGroup)
admin.site.register(models.ServiceType)
