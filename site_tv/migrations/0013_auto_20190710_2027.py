# Generated by Django 2.2.2 on 2019-07-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_tv', '0012_auto_20190710_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='kwargs**',
        ),
        migrations.AddField(
            model_name='post',
            name='post_dates',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
