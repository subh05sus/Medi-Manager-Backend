# Generated by Django 4.2.7 on 2024-04-13 09:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking_slot", "0010_slot_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="slot",
            old_name="booking_slot",
            new_name="booking_config_id",
        ),
        migrations.AlterUniqueTogether(
            name="slot",
            unique_together={("booking_config_id", "session_type", "slot_number")},
        ),
    ]
