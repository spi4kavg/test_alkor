# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0003_auto_20150302_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='instance',
            new_name='instances',
        ),
    ]
