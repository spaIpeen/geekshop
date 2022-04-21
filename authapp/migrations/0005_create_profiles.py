from django.db import migrations, transaction


def forwards_func(apps, schema_editor):
    try:
        ShopUser = apps.get_model("authapp", "ShopUser")
        ShopUserProfile = apps.get_model("authapp", "ShopUserProfile")

        with transaction.atomic():
            qs = ShopUser.objects.all()
            for item in qs:
                ShopUserProfile.objects.create(user=item)
    except Exception as exp:
        print(f"Cann't create user profile: {exp}")


def reverse_func(apps, schema_editor):
    try:
        ShopUserProfile = apps.get_model("authapp", "ShopUserProfile")

        with transaction.atomic():
            ShopUserProfile.objects.all().delete()
    except Exception as exp:
        print(f"Cann't delete users profiles: {exp}")


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0004_user_profile"),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
