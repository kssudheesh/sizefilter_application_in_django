# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sizefilter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_variants',
            old_name='product',
            new_name='product_id',
        ),
        migrations.RemoveField(
            model_name='product_variants',
            name='text',
        ),
    ]
