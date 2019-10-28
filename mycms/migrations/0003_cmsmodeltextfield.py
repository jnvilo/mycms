# Generated by Django 2.2.6.dev20190909114231 on 2019-10-18 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("mycms", "0002_cmscontentmodelfield_cmsmodelfield")]

    operations = [
        migrations.CreateModel(
            name="CMSModelTextField",
            fields=[
                (
                    "cmsmodelfield_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="mycms.CMSModelField",
                    ),
                ),
                (
                    "content",
                    models.TextField(default="No Content", max_length=4096, null=True),
                ),
            ],
            bases=("mycms.cmsmodelfield",),
        )
    ]
