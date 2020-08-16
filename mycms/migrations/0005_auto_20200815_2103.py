# Generated by Django 2.2.13 on 2020-08-15 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycms', '0004_cmsentries_logo_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsentries',
            name='draft',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cmsentries_draft', to='mycms.CMSContents'),
        ),
        migrations.AlterField(
            model_name='cmsentries',
            name='content',
            field=models.ManyToManyField(blank=True, related_name='cmsentries_content', to='mycms.CMSContents'),
        ),
    ]
