# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Seller(models.Model):
    name = models.CharField(u'nome do fornecedor', max_length=100)

    class Meta:
        verbose_name = u'fornecedor'
        verbose_name_plural = u'fornecedores'


class ServiceCategory(models.Model):
    name = models.CharField(u'categoria', max_length=50)

    class Meta:
        verbose_name = u'categoria'
        verbose_name_plural = u'categorias'


class Service(models.Model):
    seller = models.ForeignKey(Seller, verbose_name=u'fornecedor')
    name = models.CharField(u'nome do serviço', max_length=100)
    description = models.CharField(u'descricao do serviço', max_length=500)
    price = models.DecimalField(
        u'preco', max_digits=19, decimal_places=2
    )
    category = models.ForeignKey(ServiceCategory, verbose_name=u'categoria')
    rating = models.DecimalField(
        u'nota do serviço',
        blank=True,
        decimal_places=1,
        max_digits=3,
        null=True,
        validators=[
            MinValueValidator(Decimal('0.0')),
            MaxValueValidator(Decimal('5.0'))
        ]
    )

    class Meta:
        verbose_name = u'serviço'
