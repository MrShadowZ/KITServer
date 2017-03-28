# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_teacher_middle_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cabinet',
            options={'ordering': ['number'], 'verbose_name': 'Кабинет', 'verbose_name_plural': 'Кабинеты'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['name'], 'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['last_name', 'first_name', 'middle_name'], 'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
    ]
