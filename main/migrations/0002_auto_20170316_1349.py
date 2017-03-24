# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 12:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='trasnferAmount',
            new_name='transferAmount',
        ),
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='report',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Kasa', to='main.Book', verbose_name='Kasa'),
        ),
        migrations.AlterField(
            model_name='report',
            name='fromDate',
            field=models.DateField(default=datetime.datetime(2017, 3, 1, 0, 0), verbose_name='Data od'),
        ),
        migrations.AlterField(
            model_name='report',
            name='toDate',
            field=models.DateField(default=datetime.datetime(2017, 3, 31, 0, 0), verbose_name='Data do'),
        ),
    ]