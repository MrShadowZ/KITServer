# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chedule', '0002_auto_20170328_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayChedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='teachlesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.Teacher', verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='eight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eight', to='chedule.TeachLesson', verbose_name='15:35 - 16:20'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='five',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='five', to='chedule.TeachLesson', verbose_name='13:00 - 13:45'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='four',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='four', to='chedule.TeachLesson', verbose_name='11:45 - 12:30'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='nine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nine', to='chedule.TeachLesson', verbose_name='16:25 - 17:10'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='one', to='chedule.TeachLesson', verbose_name='09:00 - 09:45'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='seven',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seven', to='chedule.TeachLesson', verbose_name='14:45 - 15:30'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='six',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='six', to='chedule.TeachLesson', verbose_name='13:50 - 14:35'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='ten',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ten', to='chedule.TeachLesson', verbose_name='17:15 - 18:00'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='three',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='three', to='chedule.TeachLesson', verbose_name='10:55 - 11:40'),
        ),
        migrations.AddField(
            model_name='daychedule',
            name='two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='two', to='chedule.TeachLesson', verbose_name='09:50 - 10:35'),
        ),
    ]
