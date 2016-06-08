# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 19:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=120)),
                ('place', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=280)),
                ('phone', models.CharField(default=None, max_length=20, null=True)),
                ('website', models.URLField(default=None, max_length=120, null=True)),
                ('price', models.CharField(default=None, max_length=5, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('show', models.BooleanField(default=True)),
                ('vote', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=280)),
                ('phone', models.CharField(max_length=120)),
                ('website', models.URLField(max_length=150)),
                ('industry', models.CharField(max_length=120)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cal.Events')),
            ],
        ),
        migrations.CreateModel(
            name='TaggedTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='taggedtag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cal.Tags'),
        ),
    ]