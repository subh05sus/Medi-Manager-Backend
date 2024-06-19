# Generated by Django 4.2.7 on 2024-05-06 13:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("appointment", "0013_alter_appointment_booking_slot"),
        ("test_report", "0003_alter_testreport_document_path"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="testreport",
            unique_together={("user_id", "appointment_id", "document_label")},
        ),
    ]
