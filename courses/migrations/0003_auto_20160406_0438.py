# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 04:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20160406_0243'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='nome',
            new_name='name',
        ),
    ]