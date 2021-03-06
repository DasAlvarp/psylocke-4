# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memberName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judge', models.CharField(max_length=200)),
                ('score1', models.DecimalField(decimal_places=1, max_digits=2)),
                ('score2', models.DecimalField(decimal_places=1, max_digits=2)),
                ('score3', models.DecimalField(decimal_places=1, max_digits=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ScoringCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteriaName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=200)),
                ('category', models.ManyToManyField(to='main.Category')),
                ('member', models.ManyToManyField(blank=True, to='main.Member')),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='teamName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Team'),
        ),
        migrations.AddField(
            model_name='category',
            name='criteria',
            field=models.ManyToManyField(blank=True, to='main.ScoringCriteria'),
        ),
    ]
