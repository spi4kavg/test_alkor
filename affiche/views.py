# -*- coding: utf8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, Category
from serializers import EventSerializer, CategoriesSerializer, CustomPaginationSerializer


def home(request):
    return render(request, 'affiche/index.html', {})


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_serializer_class = CustomPaginationSerializer
    paginate_by_param = 'per_page'
    paginate_by = 20

    def get_queryset(self):
        fltr = {}
        if self.request.GET.get('category'):
            fltr = {
                'categories__id': self.request.GET.get('category'),
            }
        return self.queryset.filter(**fltr)


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer