# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsblog', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('event_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('abstract', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('zip', models.CharField(max_length=128)),
                ('contact_name', models.CharField(max_length=128)),
                ('contact_phone', models.CharField(max_length=128)),
                ('contact_email', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]