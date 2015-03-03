# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0004_auto_20150302_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='instances',
            field=models.ManyToManyField(related_name=b'instances', verbose_name='\u0418\u043d\u0441\u0442\u0430\u043d\u0441\u044b', to=b'affiche.Instance'),
        ),
    ]
