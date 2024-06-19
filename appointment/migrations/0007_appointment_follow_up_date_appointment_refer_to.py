# Generated by Django 4.2.7 on 2024-03-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appointment", "0006_alter_appointment_specialization_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="follow_up_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="appointment",
            name="refer_to",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
