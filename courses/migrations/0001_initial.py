# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descriçao')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Date de inicio')),
                ('image', models.ImageField(upload_to='courses/images', verbose_name='Imagem')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Criado em')),
            ],
        ),
    ]
