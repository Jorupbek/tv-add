# Generated by Django 2.2.3 on 2019-07-19 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_tv', '0029_auto_20190719_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]
