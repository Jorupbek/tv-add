# Generated by Django 2.2.3 on 2019-07-19 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_tv', '0028_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
