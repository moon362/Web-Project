# Generated by Django 4.1.1 on 2023-03-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0019_page"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("news", models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name="Page",
        ),
    ]
