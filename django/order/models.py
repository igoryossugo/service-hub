# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from customer.models import Customer
from service.models import Service

from django.db import models


class OrderStatus(models.Model):
    description = models.CharField(max_length=50)


class Order(models.Model):
    service = models.ForeignKey(Service)
    customer = models.ForeignKey(Customer)
    status = models.ForeignKey(OrderStatus)
    date = models.DateField(auto_now_add=True)
