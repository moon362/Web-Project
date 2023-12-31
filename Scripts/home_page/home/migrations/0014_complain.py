# Generated by Django 4.1.1 on 2023-03-15 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0013_alter_roomnumber_roomno"),
    ]

    operations = [
        migrations.CreateModel(
            name="Complain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("registration_no", models.CharField(max_length=50)),
                ("room_no", models.CharField(max_length=50)),
                ("complaint", models.TextField()),
            ],
        ),
    ]
