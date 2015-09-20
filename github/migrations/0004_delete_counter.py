# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0003_auto_20150918_1632'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Counter',
        ),
    ]
