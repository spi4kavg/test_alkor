# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='instance',
            field=models.ManyToManyField(to='affiche.Instance', verbose_name='\u0418\u043d\u0441\u0442\u0430\u043d\u0441\u044b'),
            preserve_default=True,
        ),
    ]
