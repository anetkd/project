# Generated by Django 5.2a1 on 2025-03-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Concert",
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
                ("artist", models.CharField(max_length=100)),
                ("date", models.DateTimeField()),
                ("venue", models.CharField(max_length=200)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
