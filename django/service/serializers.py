# -*- coding: utf-8 -*-
from rest_framework import serializers
from model import Seller, Service, ServiceCategory


class SellerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Seller.objects.create(**validated_data)


class ServiceCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return ServiceCategory.objects.create(**validated_data)


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    price = serializers.DecimalField(decimal_places=2)
    category = ServiceCategorySerializer()
    rating = serializers.DecimalField(
        blank=True,
        decimal_places=1,
        max_digits=3,
        null=True
    )

    def create(self, validated_data):
        return Service.objects.create(**validated_data)
