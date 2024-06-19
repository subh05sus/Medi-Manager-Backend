# Generated by Django 4.2.7 on 2024-04-13 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "booking_slot",
            "0006_alter_bookingslot_unique_together_bookingslot_day_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="bookingslot",
            name="doctor_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="booking_slots",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
