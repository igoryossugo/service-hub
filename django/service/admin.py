# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Seller, Service, ServiceCategory


class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('seller', 'name', 'category')
    list_display = ('name', 'seller', 'category', 'review', 'price')


class SellerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


class ServiceCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
