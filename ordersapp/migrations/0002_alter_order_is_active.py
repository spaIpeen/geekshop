# Generated by Django 3.2.12 on 2022-04-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ordersapp", "0001_orders"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="is_active",
            field=models.BooleanField(db_index=True, default=True, verbose_name="активен"),
        ),
    ]