# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-13 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0019_add_stripe_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fare',
            name='threshold',
            field=models.IntegerField(default=-1),
        ),
    ]
