# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_remove_counter_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
