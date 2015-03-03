# -*- coding: utf8 -*-
from .models import Event, Instance, Place, City, Category
from rest_framework import serializers, pagination


class CustomMetaSerializer(serializers.Serializer):
    has_next_page = serializers.ReadOnlyField(source='has_next')
    has_prev_page = serializers.ReadOnlyField(source='has_previous')


class CustomPaginationSerializer(pagination.BasePaginationSerializer):
    pagination = CustomMetaSerializer(source='*')
    results_field = 'data'


class City(serializers.ModelSerializer):

    class Meta:
        model = City


class PlaceSerializer(serializers.ModelSerializer):

    city = City()

    class Meta:
        model = Place


class InstanceSerializer(serializers.ModelSerializer):

    place = PlaceSerializer()

    class Meta:
        model = Instance
        exclude = ("id",)


class EventSerializer(serializers.ModelSerializer):

    instances = InstanceSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        exclude = ("categories",)


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category