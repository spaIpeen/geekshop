# Generated by Django 3.2.12 on 2022-04-15 08:08

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0002_user_model_extend"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 4, 17, 8, 8, 8, 113251, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
        migrations.AlterField(
            model_name="shopuser",
            name="age",
            field=models.PositiveIntegerField(default=18, verbose_name="возраст"),
        ),
    ]
