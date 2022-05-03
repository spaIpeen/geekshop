# Generated by Django 3.2.12 on 2022-04-29 16:45

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0006_alter_shopuser_activation_key_expires"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 5, 1, 16, 45, 56, 493701, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
    ]