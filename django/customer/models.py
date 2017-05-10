# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    name = models.CharField(u'nome do consumidor', max_length=200)
    cpf = models.CharField(u'cpf', max_length=30)
    email = models.EmailField(u'email do consumidor')
