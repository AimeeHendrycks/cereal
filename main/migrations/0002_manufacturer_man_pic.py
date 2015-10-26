# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturer',
            name='man_pic',
            field=models.ImageField(null=True, upload_to=b'man_pic', blank=True),
        ),
    ]
