# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-11 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CMSContents",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=1024, null=True)),
                ("content", models.TextField(default="Empty", max_length=20480)),
                ("timestamp", models.DateTimeField(auto_now=True)),
                (
                    "meta_description",
                    models.TextField(blank=True, default="", max_length=20480),
                ),
                ("page", models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name="CMSEntries",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(default=None, max_length=1024)),
                ("slug", models.SlugField(max_length=1024, unique=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now_add=True)),
                ("frontpage", models.BooleanField(default=False)),
                ("published", models.BooleanField(default=False)),
                ("page_number", models.IntegerField(default=1)),
                ("content", models.ManyToManyField(blank=True, to="mycms.CMSContents")),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CMSMarkUps",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("markup", models.CharField(default="Creole", max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="CMSPageTypes",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_type", models.CharField(default="DefaultType", max_length=64)),
                ("text", models.CharField(default="default class", max_length=128)),
                ("view_class", models.CharField(default="DefaultView", max_length=256)),
                ("view_template", models.CharField(default=None, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="CMSPaths",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("path", models.CharField(max_length=2000, null=True)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="mycms.CMSPaths",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CMSTags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="NotSet", max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="CMSTemplates",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="page.html", max_length=1024)),
                (
                    "template",
                    models.TextField(default="empty template", max_length=10240),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cmsentries",
            name="page_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="mycms.CMSPageTypes",
            ),
        ),
        migrations.AddField(
            model_name="cmsentries",
            name="path",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="mycms.CMSPaths",
            ),
        ),
        migrations.AddField(
            model_name="cmsentries",
            name="template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="mycms.CMSTemplates",
            ),
        ),
        migrations.AddField(
            model_name="cmscontents",
            name="markup",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="mycms.CMSMarkUps",
            ),
        ),
        migrations.AddField(
            model_name="cmscontents",
            name="tags",
            field=models.ManyToManyField(blank=True, to="mycms.CMSTags"),
        ),
    ]
