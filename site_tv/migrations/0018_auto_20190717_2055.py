# Generated by Django 2.2.3 on 2019-07-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_tv', '0017_auto_20190717_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_dates',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
