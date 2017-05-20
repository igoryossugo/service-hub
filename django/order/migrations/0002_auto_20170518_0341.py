# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'pedido'},
        ),
        migrations.AlterModelOptions(
            name='orderstatus',
            options={'verbose_name': 'status'},
        ),
        migrations.AddField(
            model_name='order',
            name='negotiated_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='preco negociado'),
        ),
    ]