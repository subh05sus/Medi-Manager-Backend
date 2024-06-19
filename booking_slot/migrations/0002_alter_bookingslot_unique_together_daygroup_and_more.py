# Generated by Django 4.2.7 on 2024-04-09 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("booking_slot", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="bookingslot",
            unique_together=set(),
        ),
        migrations.CreateModel(
            name="DayGroup",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "days",
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
                        max_length=20,
                    ),
                ),
                (
                    "doctor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("doctor_id", "days")},
            },
        ),
        migrations.RemoveField(
            model_name="bookingslot",
            name="day",
        ),
        migrations.RemoveField(
            model_name="bookingslot",
            name="doctor_id",
        ),
        migrations.AddField(
            model_name="bookingslot",
            name="day_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="booking_slot.daygroup",
            ),
        ),
    ]
