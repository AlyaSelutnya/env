# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-01-11 23:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_migrate_translatable_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorytranslation',
            old_name='_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='categorytranslation',
            old_name='_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='producttranslation',
            old_name='_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='producttranslation',
            old_name='_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='producttranslation',
            old_name='_slug',
            new_name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
