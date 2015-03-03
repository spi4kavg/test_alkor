from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CategoriesViewSet


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'categories', CategoriesViewSet)


urlpatterns = patterns('',
    url(r'^$', 'affiche.views.home', name='home'),
    url(r'^api/', include(router.urls)),
)