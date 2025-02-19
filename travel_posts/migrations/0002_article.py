# Generated by Django 5.1.4 on 2025-01-14 13:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("travel_posts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("author", models.CharField(max_length=100)),
                ("publish_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
