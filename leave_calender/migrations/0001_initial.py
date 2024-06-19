# Generated by Django 4.2.7 on 2024-04-12 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("entity", "0006_alter_entity_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppliedLeave",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("purpose", models.CharField(blank=True, max_length=60, null=True)),
                ("startDate", models.DateField()),
                ("endDate", models.DateField()),
                (
                    "entity_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="entity.entity",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
