# Generated by Django 2.2.6.dev20190909114231 on 2019-10-14 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagetype',
            old_name='default_template',
            new_name='template',
        ),
    ]