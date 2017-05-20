# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from customer.models import Customer
from service.models import Service

from django.db import models


class OrderStatus(models.Model):
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name = u'status'


class Order(models.Model):
    service = models.ForeignKey(Service, verbose_name=u'serviço')
    customer = models.ForeignKey(Customer, verbose_name=u'cliente')
    status = models.ForeignKey(OrderStatus, verbose_name=u'status')
    date = models.DateField(auto_now_add=True)
    negotiated_price = models.DecimalField(
        u'preco negociado',
        max_digits=19,
        decimal_places=2,
        default=0
    )

    class Meta:
        verbose_name = 'pedido'
