# Generated by Django 2.0 on 2017-12-30 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20171230_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
    ]
