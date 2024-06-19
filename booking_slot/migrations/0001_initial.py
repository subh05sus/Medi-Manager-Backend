# Generated by Django 4.2.7 on 2024-04-08 13:14

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
            name="BookingSlot",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("mon", "Monday"),
                            ("tue", "Tuesday"),
                            ("wed", "Wednesday"),
                            ("thu", "Thursday"),
                            ("fri", "Friday"),
                            ("sat", "Saturday"),
                            ("sun", "Sunday"),
                        ],
                        max_length=3,
                    ),
                ),
                ("morning_slots_is_active", models.BooleanField(default=True)),
                ("morning_start_time", models.TimeField(blank=True, null=True)),
                ("morning_end_time", models.TimeField(blank=True, null=True)),
                ("afternoon_slots_is_active", models.BooleanField(default=True)),
                ("afternoon_start_time", models.TimeField(blank=True, null=True)),
                ("afternoon_end_time", models.TimeField(blank=True, null=True)),
                ("evening_slots_is_active", models.BooleanField(default=True)),
                ("evening_start_time", models.TimeField(blank=True, null=True)),
                ("evening_end_time", models.TimeField(blank=True, null=True)),
                ("morning_slots", models.IntegerField(default=0)),
                ("afternoon_slots", models.IntegerField(default=0)),
                ("evening_slots", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "doctor_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("day", "is_active")},
            },
        ),
    ]
