# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Seller(models.Model):
    name = models.CharField(u'nome do comerciante', max_length=100)


class ServiceCategory(models.Model):
    name = models.CharField(u'nome do servico', max_length=50)


class ServiceReview(models.Model):
    rating = models.DecimalField(
        u'nota do servico',
        decimal_places=1,
        max_digits=3,
        null=True,
        validators=[
            MinValueValidator(Decimal('0.0')),
            MaxValueValidator(Decimal('5.0'))
        ]
    )
    comment = models.CharField(u'comentario', max_length=500)


class Service(models.Model):
    seller = models.ForeignKey(Seller)
    name = models.CharField(u'nome do servico', max_length=100)
    description = models.CharField(u'descricao do servico', max_length=500)
    price = models.DecimalField(
        u'preco original', max_digits=19, decimal_places=2
    )
    negotiated_price = models.DecimalField(
        u'preco negociado', max_digits=19, decimal_places=2
    )
    category = models.ForeignKey(ServiceCategory)
    review = models.ForeignKey(ServiceReview)
