# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_manufacturer_man_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='cereal',
            name='cereal_pic',
            field=models.ImageField(null=True, upload_to=b'cereal_pic', blank=True),
        ),
    ]
