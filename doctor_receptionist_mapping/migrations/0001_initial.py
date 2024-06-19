# Generated by Django 4.2.7 on 2024-03-04 09:10

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
            name="DoctorReceptionistMapping",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "doctor_data",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor_detail",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "receptionist_data",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receptionist_detail",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]