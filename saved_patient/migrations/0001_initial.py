# Generated by Django 4.2.7 on 2024-04-08 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SavedPatient",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("tag", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "doctor_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "patient_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]