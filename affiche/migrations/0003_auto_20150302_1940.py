# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0002_event_instance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='end',
            field=models.DateTimeField(null=True, verbose_name='\u041a\u043e\u043d\u0435\u0446 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f', blank=True),
        ),
    ]
