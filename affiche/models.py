# -*- coding: utf8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class City(models.Model):
    name = models.CharField(max_length=100,
        verbose_name=_(u"Название города"))

    class Meta:
        verbose_name = _(u"Город")

    def __unicode__(self):
        return u"{0}".format(self.name,)


class Place(models.Model):
    name = models.CharField(max_length=100,
        verbose_name=_(u"Название места"))
    lat = models.FloatField(
        verbose_name=_(u"Широта"))
    long = models.FloatField(
        verbose_name=_(u"Долгота"))
    city = models.ForeignKey(City,
        verbose_name=_(u"Город"))

    class Meta:
        verbose_name = _(u"Место проведения")
        verbose_name_plural = _(u"Места проведения")

    def __unicode__(self):
        return u"{0}".format(self.name,)


class Instance(models.Model):
    start = models.DateTimeField(
        verbose_name=_(u"Начало проведения мероприятия"))
    end = models.DateTimeField(null=True, blank=True,
        verbose_name=_(u"Конец проведения мероприятия"))
    place = models.ForeignKey(Place,
        verbose_name=_(u"Место проведения"))

    class Meta:
        verbose_name = _(u"Инстанс")
        verbose_name_plural = _(u"Инстансы")

    def __unicode__(self):
        return u"{0} {1} ({2} - {3})".format(
            self.place.city.name,
            self.place.name,
            self.start.strftime("%d.%m.%Y %H:%m"),
            self.end.strftime("%d.%m.%Y %H:%m") if self.end else u"Не указано",
        )


class Category(models.Model):
    name = models.CharField(max_length=200,
        verbose_name=_(u"Название"))

    class Meta:
        verbose_name = _(u"Категория")
        verbose_name_plural = _(u"Категории")

    def __unicode__(self):
        return u"{0}".format(self.name,)


class Event(models.Model):
    title = models.CharField(max_length=100,
        verbose_name=_(u"Название события"))
    description = models.TextField(
        verbose_name=_(u"Описание события"))
    instances = models.ManyToManyField(Instance, related_name='instances',
        verbose_name=_(u"Инстансы"))
    categories = models.ManyToManyField(Category, related_name='categories',
        verbose_name=_(u"Категории"))

    class Meta:
        verbose_name = _(u"Событие")
        verbose_name_plural = _(u"События")

    def __unicode__(self):
        return u"{0}".format(self.title,)