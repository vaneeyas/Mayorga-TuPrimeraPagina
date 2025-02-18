# Generated by Django 5.1.6 on 2025-02-17 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("titulo", models.CharField(max_length=200)),
                ("contenido", models.TextField()),
                ("fecha_publicacion", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
