# -*- coding: utf-8 -*-
# Generated by Django 2.1 on 2018-09-13 20:05
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("lists", "0005_auto_20180815_1045")]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="list",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="lists.List",
            ),
        )
    ]
